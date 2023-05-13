# spacex-api-data
Extracting and analyzing data about the SpaceX rocket launches since 2006.
Source data: https://api.spacexdata.com/v5/launches/

I used Python 3.10.8 for this script.

## How to run
Run the following commands:
1. `make venv`
2. `source .venv/bin/activate`
3. `export PYTHONPATH="$PWD"`
4. `make build-all`
5. `make build-docker-image`
6. `make open-db-for-localhost`

Environment has been set up we are ready to run scripts! Database is availabel on localhost:5432!

### Load data to database.
    `python scripts/load.py`

### Generate reports
    `python scripts/analyze.py`


Results are stored in reports folder!