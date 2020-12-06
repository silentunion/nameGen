from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api

from . import db_request as req

app = Flask(__name__)
api = Api(app)
CORS(app)

class Letters(Resource):
    def get(self):
        try:
            items = req.get_letters()
        except:
            items = [{'letter': "No letters were found"}]
        return items

api.add_resource(Letters, '/letters')

app.run(port=5000)
