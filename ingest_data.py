import requests

from elitedata.fixtures.fixture_fixer import fix_all

__author__ = 'Jingyu_Yao'

# eddb.io data locations
commodities = "http://eddb.io/archive/v3/commodities.json"
systems = "http://eddb.io/archive/v3/systems.json"
stations_lite = "http://eddb.io/archive/v3/stations_lite.json"

fixture_directory = "elitedata/fixtures/"

def get_and_save(url):
    file_name = url.split('/')[-1]
    r = requests.get(url)
    with open(fixture_directory + file_name, 'wt') as f:
        f.write(r.text)


def ingest():
    get_and_save(commodities)
    get_and_save(systems)
    get_and_save(stations_lite)

    fix_all(fixture_directory)

if __name__ == "__main__":
    ingest()