from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api

from . import db_request as req
from ..gen import basic

app = Flask(__name__)
api = Api(app)
CORS(app)


class NamesTemplate(Resource):
    def get(self, template, num):
        items = {'template': template,
                'num': num,
                'is_weighted': False,
                'is_random': False}
        try:
            names = basic.generate_from_template(**items)
        except:
            names = [{'name': 'Something went wrong'}]
        return names

class NamesTemplateWeighted(Resource):
    def get(self, template, num):
        items = {'template': template,
                'num': num,
                'is_weighted': True,
                'is_random': False}
        try:
            names = basic.generate_from_template(**items)
        except:
            names = [{'name': 'Something went wrong'}]
        return names

class NamesRandom(Resource):
    def get(self, num):
        items = {'template': False,
                'num': num,
                'is_weighted': False,
                'is_random': True}
        try:
            names = basic.generate_random(**items)
        except:
            names = [{'name': 'Something went wrong'}]
        return names

class NamesRandomWeighted(Resource):
    def get(self, num):
        items = {'template': False,
                'num': num,
                'is_weighted': True,
                'is_random': True}
        try:
            names = basic.generate_random(**items)
        except:
            names = [{'name': 'Something went wrong'}]
        return names


api.add_resource(NamesTemplate, '/basic/num=<int:num>&temp=<string:template>')
api.add_resource(NamesTemplateWeighted, '/basic/num=<int:num>&temp=<string:template>&w')
api.add_resource(NamesRandom, '/basic/num=<int:num>')
api.add_resource(NamesRandomWeighted, '/basic/num=<int:num>&w')

app.run(port=5000)
