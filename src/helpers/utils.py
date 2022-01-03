from jsonschema import validate

def validate_request_data(request_schema: object, request_data):
    validate(request_data, request_schema)
