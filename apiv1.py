from flask import Blueprint
from flask_restplus import Api

from apis.stringvalidation import api as ns1

api = Api(
    title='String Validation',
    version='1.0',
    description='To test the string',
    # All API metadatas
)

v1 = Blueprint("apiv1", __name__, url_prefix="/v1")

api = Api(v1,
          title="String API",
          version='v1',
          description="String API service."
          )

api.add_namespace(ns1)
