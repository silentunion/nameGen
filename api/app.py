from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Letters(Resource):
    def get(self, letter):
        return {'letter': letter}

api.add_resource(Letters, '/letter/<string:letter>')

app.run(port=5000)
