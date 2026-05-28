import json

class SchemaValidator:

    def validate(self, payload, schema):

        required = schema.get("required", [])

        for field in required:
            if field not in payload:
                return False

        return True
