import logging
import json

import pandas as pd

from scripts.utils import PostgresConnector

def main():
    with PostgresConnector() as pg:
        data = pd.read_json('spacex.json')
        pg.load_data(data, 'api')










if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
    main()