from flask import Flask
from flask_restx import Resource, Api, fields, reqparse
from http import HTTPStatus

from namespaces.fruit import api as fruit_api
from namespaces.vegetable import api as vegetable_api


app = Flask(__name__)
api = Api(app, version="1.0", title="Fruit&Veg", description="Random fruits and vegetables generator")


api.add_namespace(fruit_api, path='/fruit')
api.add_namespace(vegetable_api, path='/vegetable')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5016, debug=True)