import logging

from scripts.utils import PostgresConnector


def main():
    generate_report('max_core_reuse')
    generate_report('cores_reused_less_than_50_days')
    generate_report('more_than_one_launch_by_month')


def generate_report(file_name: str):
    with PostgresConnector() as pg:
        df = pg.select(f'queries/{file_name}.sql')
        df.to_csv(f'reports/{file_name}.xlsx', index=False)
    logging.info(f'Report for {file_name} is done.')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
    main()
