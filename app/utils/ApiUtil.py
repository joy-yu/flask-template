from flask import json
from werkzeug.wrappers import Response
from app.utils.DateUtil import DateTimeEncoder

class ApiResult(object):

    def __init__(self, value, status=200):
        self.value = value
        self.status = status

    def to_response(self):
        return Response(json.dumps(self.value, cls=DateTimeEncoder),
                        status=self.status,
                        mimetype='application/json')