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

class WordsTemplate(Resource):
    def get(self, template, num, is_weighted=False):
        items = basic.generate(num, is_weighted, False, template)
        return items

class WordsTemplateWeighted(Resource):
    def get(self, template, num, is_weighted=True):
        items = basic.generate(num, is_weighted, False, template)
        return items

class RandomWords(Resource):
    def get(self, num, is_weighted=False):
        items = basic.generate(num, is_weighted)
        return items

class RandomWordsWeighted(Resource):
    def get(self, num, is_weighted=True):
        items = basic.generate(num, is_weighted)
        return items

class Nonestuff(Resource):
    def get(self, num):
        items = [{'Bob'}]
        return items

api.add_resource(Letters, '/letters')
api.add_resource(WordsTemplate, '/words/false/<int:num>/<string:template>')
api.add_resource(WordsTemplateWeighted, '/words/true/<int:num>/<string:template>')
api.add_resource(RandomWords, '/words/false/<int:num>')
api.add_resource(RandomWordsWeighted, '/words/true/<int:num>')
api.add_resource(Nonestuff, '/words/<int:num>/')

app.run(port=5000)
