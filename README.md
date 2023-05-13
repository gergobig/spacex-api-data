# spacex-api-data
Extracting and analyzing data about the SpaceX rocket launches since 2006.
Source data: https://api.spacexdata.com/v5/launches/

I used Python 3.10.8 for this script.

## Build Docker image
1. `make build-docker-image`
## How to run
Run the following commands:
1. `make venv`
2. `source .venv/bin/activate`
3. `make build-all`
4. `make init-docker`