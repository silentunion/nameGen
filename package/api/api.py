from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api

from . import db_request as req
from ..gen import basic

app = Flask(__name__)
api = Api(app)
CORS(app)


class WordsTemplate(Resource):
    def get(self, template, num):
        items = {'template': template,
                'num': num,
                'is_weighted': False,
                'is_random': False}
        try:
            names = basic.generate(**items)
        except:
            names = [{'name': 'Something went wrong'}]
        return names

class WordsTemplateWeighted(Resource):
    def get(self, template, num):
        items = {'template': template,
                'num': num,
                'is_weighted': True,
                'is_random': False}
        try:
            names = basic.generate(**items)
        except:
            names = [{'name': 'Something went wrong'}]
        return names

class RandomWords(Resource):
    def get(self, num):
        items = {'template': False,
                'num': num,
                'is_weighted': False,
                'is_random': True}
        try:
            names = basic.generate(**items)
        except:
            names = [{'name': 'Something went wrong'}]
        return names

class RandomWordsWeighted(Resource):
    def get(self, num):
        items = {'template': False,
                'num': num,
                'is_weighted': True,
                'is_random': True}
        try:
            names = basic.generate(**items)
        except:
            names = [{'name': 'Something went wrong'}]
        return names


api.add_resource(WordsTemplate, '/words/false/<int:num>/<string:template>')
api.add_resource(WordsTemplateWeighted, '/words/true/<int:num>/<string:template>')
api.add_resource(RandomWords, '/words/false/<int:num>')
api.add_resource(RandomWordsWeighted, '/words/true/<int:num>')

app.run(port=5000)
