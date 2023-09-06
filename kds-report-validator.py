import json
from jsonschema import validate
from jsonschema import ValidationError

kds_schema = None
kds_report_example = None

with open("kds-report-v2-schema.json", "r") as schema_file:
    kds_schema = json.load(schema_file)

with open("kds-report-v2-example.json", "r") as example_file:
    kds_report_example = json.load(example_file)

try:
    validate(instance=kds_report_example, schema=kds_schema)

except ValidationError as validationError:
    print("Validation failed")
    print(validationError.message)
