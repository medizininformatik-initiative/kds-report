import json
from datetime import date, datetime
from urllib.parse import urlparse
import pytz
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--bundle-version', type=str, required=True)
args = parser.parse_args()
search_bundle_version = args.bundle_version

bundle = {
    "resourceType": "Bundle",
    "meta": {
        "versionId": "1",
        "lastUpdated": datetime.now(pytz.timezone('Europe/Berlin')).isoformat(),
        "profile": [
            f"http://medizininformatik-initiative.de/fhir/Bundle/search-bundle-report|{search_bundle_version}"
        ],
        "tag": [
            {
                "system": "http://dsf.dev/fhir/CodeSystem/read-access-tag",
                "code": "ALL"
            }
        ]
    },
    "identifier": {
        "system": "http://medizininformatik-initiative.de/sid/search-bundle-identifier",
        "value": f"search-bundle-v{search_bundle_version}"
    },
    "type": "batch",
    "entry": []
}


def append_year_query(query):

    cur_year = query['startYear']
    last_year = date.today().year + 2

    while cur_year <= last_year:

        parsed_url = urlparse(query['query'])
        year_query = f'{parsed_url.path}?{query["dateParam"]}=eq{str(cur_year)}&{parsed_url.query}'

        cur_query = {
            "request": {
                "method": "GET",
                "url": year_query.strip("/")
            }
        }

        bundle['entry'].append(cur_query)

        cur_year = cur_year + 1


with open("report-queries.json", "r") as report_q_file:
    report_queries = json.load(report_q_file)


for query in report_queries['statusQueries']:

    if query['type'] == 'year':
        append_year_query(query)

    else:
        cur_query = {
            "request": {
                "method": "GET",
                "url": query['query'].strip("/")
            }
        }

        bundle['entry'].append(cur_query)


bundle['entry'].append({
            "request": {
                "method": "GET",
                "url": "metadata"
            }
        })


with open(f"dsf-search-bundle_{search_bundle_version}.json", "w+") as dsf_search_bundle_file:
    json.dump(bundle, dsf_search_bundle_file)
