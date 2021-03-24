import json
import re
import sys
import unicodedata

source = "./src/data"


def remove_accents(input_str):
    # thx to https://stackoverflow.com/a/517974
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii


def timeit(function):
    def wrapper(*args):
        from time import time_ns
        start = time_ns()
        function(*args)
        print("Elapsed time:", (time_ns() - start)/1e9)
    return wrapper


@timeit
def search(query: str):
    query = remove_accents(query)
    with open(source + "/cities.json", "r", encoding='utf-8') as cities:
        cities = json.loads(cities.read())
    # with open(source + "/countries.json", "r", encoding='utf-8') as countries:
    #     countries = json.loads(countries.read())
    # with open(source + "/continents.json", "r", encoding='utf-8') as continents:
    #     continents = json.loads(continents.read())
    # with open(source + "/languages.json", "r", encoding='utf-8') as languages:
    #     languages = json.loads(languages.read())

    def find_match(city) -> bool:
        return re.search(query, remove_accents(city["name"]),
                         re.IGNORECASE | re.MULTILINE | re.L) != None

    resp = filter(find_match, cities)
    print(json.dumps(list(resp), ensure_ascii=False, indent=4))


if __name__ == "__main__":
    query = sys.argv[1]
    search(query)
