import json
from jsonschema import validate
import allure
from utils.path import schema_path


@allure.step('Validate JSON schema')
def validate_schema(response, schema):
    schema = json.load(open(schema_path(file_name=schema)))
    validate(response, schema)
