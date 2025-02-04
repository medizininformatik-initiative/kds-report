import json
import re


kds_validation_regex = "^\\/(((ResearchSubject|ResearchStudy|ImagingStudy|MedicationStatement|ServiceRequest|FamilyMemberHistory|Observation|DiagnosticReport|Patient|Composition|MedicationAdministration|Condition|MedicationRequest|Medication|List|RiskAssessment|Media|Procedure|Task|Consent|Specimen)\\?(^_summary|[^=]|_profile=|code=([^=]*)\\|&|_profile:below=|type=([^=]*)\\|&|date=[0-9]{4}(?![-]))*)|((Encounter)\\?(^_summary|[^=]|_profile=|code=([^=]*)\\|&|_profile:below=|type=|date=[0-9]{4}(?![-]))*))_summary=count"
kds_report_input_urls = {}

with open("report-queries.json", "r") as url_file:
    kds_report_input_urls = json.load(url_file)


for status_query in kds_report_input_urls['statusQueries']:
    input_url = status_query['query']

    search_result = re.search(kds_validation_regex, input_url)

    if search_result is None:
        print("######## INVALID INPUT URL")
        print(f'input url: {input_url} is not valid')
