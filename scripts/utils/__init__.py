import logging
from typing import Dict

import psycopg2
import pandas as pd
from sqlalchemy import create_engine


class PostgresConnector:
    def __init__(self, host='localhost', database='spacex', user='gbig', password='gbig'):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conn = None

    def __enter__(self):
        logging.info('Opening connection.')
        self.conn = psycopg2.connect(
            host=self.host, database=self.database, user=self.user, password=self.password
        )
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()
        logging.info('Connection closed.')

    def __read_query_from_file(self, file_path: str) -> str:
        with open(file_path, 'r', encoding='utf8') as f:
            return ' '.join(f.readlines()).replace('\n', '')

    def load_data(self, df: pd.DataFrame, table_name: str, schema: Dict[str, str]):
        engine = create_engine(
            f'postgresql+psycopg2://{self.user}:{self.password}@{self.host}:5432/{self.database}'
        )
        df.to_sql(
            table_name,
            engine,
            if_exists='replace',
            index=False,
            dtype=schema,
        )
        logging.info(f'Data has been loaded to {table_name} table.')

    def update(self, query):
        with self.conn.cursor() as cur:
            cur.execute(query)
            return cur.rowcount

    def delete(self, query):
        return self.update(query)

    def select(self, file_path: str) -> pd.DataFrame:
        query = self.__read_query_from_file(file_path)
        return pd.read_sql_query(query, self.conn)
