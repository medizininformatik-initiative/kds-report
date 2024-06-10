import json
from datetime import date, datetime
from urllib.parse import urlparse
import pytz

bundle = {
    "resourceType": "Bundle",
    "meta": {
        "versionId": "1",
        "lastUpdated": datetime.now(pytz.timezone('Europe/Berlin')).isoformat(),
        "profile": [
            "http://medizininformatik-initiative.de/fhir/Bundle/search-bundle-report|1.1"
        ],
        "tag": [
            {
                "system": "http://dsf.dev/fhir/CodeSystem/read-access-tag",
                "code": "ALL"
            }
        ]
    },
    "identifier": {
        "system": "http://medizininformatik-initiative.de/fhir/CodeSystem/report",
        "value": "search-bundle-v1.1"
    },
    "type": "batch",
    "entry": []
}


def append_year_query(query):

    cur_year = query['startYear']
    last_year = date.today().year

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


with open("dsf-search-bundle.json", "w+") as dsf_search_bundle_file:
    json.dump(bundle, dsf_search_bundle_file)
