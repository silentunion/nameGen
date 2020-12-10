from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api

from . import db_request as req
from ..gen import basic

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

class Words(Resource):
    def get(self, template, num):
        items = basic.generate(template, num)
        return items

class RandomWords(Resource):
    def get(self, num):
        items = basic.completely_random(num)
        return items

class Nonestuff(Resource):
    def get(self, num):
        items = [{'Bob'}]
        return items

api.add_resource(Letters, '/letters')
api.add_resource(Words, '/words/<int:num>/<string:template>')
api.add_resource(RandomWords, '/words/random/<int:num>')
api.add_resource(Nonestuff, '/words/<int:num>/')

app.run(port=5000)
