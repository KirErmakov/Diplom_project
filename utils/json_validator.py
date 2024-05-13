import json
from jsonschema import validate
import allure
from utils.path import relative_from_root


@allure.step('Validate JSON schema')
def validate_schema(response, schema):
    #schema = json.load(open(schema_path(file_name=schema)))
    schema = json.load(open(relative_from_root(path=schema)))
    validate(response, schema)
