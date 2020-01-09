from flask import request
from flask_restplus import Namespace, Resource, reqparse, fields

from lib.validator import Validator

api = Namespace("stringvalidation", "String related operations")

@api.route("/<string:data>")
class StringValidation(Resource):
    def post(self, data):
        """
        Pass string and return filtered result
        """
        result = Validator(data).run()
        if result['message'] == 'Error':
            return result, 400
        return result, 200
