from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api

from . import db_request as req
from ..gen import basic

app = Flask(__name__)
api = Api(app)
CORS(app)


class WordsTemplate(Resource):
    def get(self, template, num, is_weighted=False):
        try:
            items = basic.generate(num, is_weighted, False, template)
        except:
            items = [{'name': 'Something went wrong'}]
        return items

class WordsTemplateWeighted(Resource):
    def get(self, template, num, is_weighted=True):
        try:
            items = basic.generate(num, is_weighted, False, template)
        except:
            items = [{'name': 'Something went wrong'}]
        return items

class RandomWords(Resource):
    def get(self, num, is_weighted=False):
        try:
            items = basic.generate(num, is_weighted)
        except:
            items = [{'name': 'Something went wrong'}]
        return items

class RandomWordsWeighted(Resource):
    def get(self, num, is_weighted=True):
        try:
            items = basic.generate(num, is_weighted)
        except:
            items = [{'name': 'Something went wrong'}]
        return items


api.add_resource(WordsTemplate, '/words/false/<int:num>/<string:template>')
api.add_resource(WordsTemplateWeighted, '/words/true/<int:num>/<string:template>')
api.add_resource(RandomWords, '/words/false/<int:num>')
api.add_resource(RandomWordsWeighted, '/words/true/<int:num>')

app.run(port=5000)
