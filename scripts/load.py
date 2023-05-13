import logging

import pandas as pd
from sqlalchemy.types import JSON, TEXT, DOUBLE_PRECISION, BOOLEAN, ARRAY, BIGINT

from scripts.utils import PostgresConnector

SCHEMA = {
    'fairings': JSON,
    'links': JSON,
    'static_fire_date_utc': TEXT,
    'static_fire_date_unix': DOUBLE_PRECISION,
    'net': BOOLEAN,
    'window': DOUBLE_PRECISION,
    'rocket': TEXT,
    'success': DOUBLE_PRECISION,
    'failures': ARRAY(JSON),
    'details': TEXT,
    'crew': ARRAY(JSON),
    'ships': ARRAY(TEXT),
    'capsules': ARRAY(TEXT),
    'payloads': ARRAY(TEXT),
    'launchpad': TEXT,
    'flight_number': BIGINT,
    'name': TEXT,
    'date_utc': TEXT,
    'date_unix': BIGINT,
    'date_local': TEXT,
    'date_precision': TEXT,
    'upcoming': BOOLEAN,
    'cores': ARRAY(JSON),
    'auto_update': BOOLEAN,
    'tbd': BOOLEAN,
    'launch_library_id': TEXT,
    'id': TEXT,
}


def main():
    with PostgresConnector() as pg:
        pg.load_data(pd.read_json('spacex.json'), table_name='api', schema=SCHEMA)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
    main()
