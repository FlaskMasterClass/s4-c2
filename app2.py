from flask_restx import Namespace, Resource, fields
from flask import Flask
from flask_restx import Resource, Api, fields, reqparse


app = Flask(__name__)
api = Api(app, version="1.0", title="Fruit&Veg", description="Random fruits and vegetables generator")


capi = Namespace('cats', description='Cats related operations')

cat = api.model('Cat', {
    'id': fields.String(required=True, description='The cat identifier'),
    'name': fields.String(required=True, description='The cat name'),
})

CATS = [
    {'id': 'felix', 'name': 'Felix'},
]

@capi.route('/')
class CatList(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(cat)
    def get(self):
        '''List all cats'''
        return CATS

@capi.route('/<id>')
@capi.param('id', 'The cat identifier')
@capi.response(404, 'Cat not found')
class Cat(Resource):
    @api.doc('get_cat')
    @api.marshal_with(cat)
    def get(self, id):
        '''Fetch a cat given its identifier'''
        for cat in CATS:
            if cat['id'] == id:
                return cat
        api.abort(404)


api.add_namespace(capi, path='/cat')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5015, debug=True)