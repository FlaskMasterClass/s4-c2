from flask_restx import Namespace, Resource, fields
from flask import Flask
from flask_restx import Resource, Api, fields, reqparse


app = Flask(__name__)
api = Api(app, version="1.0", title="Fruit&Veg", description="Random fruits and vegetables generator")


authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
    }
}

capi = Namespace('cats', description='Cats related operations', authorizations=authorizations)

cat = api.model('Cat', {
    'id': fields.String(required=True, description='The cat identifier'),
    'name': fields.String(required=True, description='The cat name'),
})

CATS = [
    {'id': 'felix', 'name': 'Felix'},
]

@capi.route('/')
class CatList(Resource):
    @capi.doc(security="apiKey")
    @capi.doc('list_cats')
    @capi.marshal_list_with(cat)
    def get(self):
        '''List all cats'''
        return CATS

@capi.route('/<id>')
@capi.param('id', 'The cat identifier')
@capi.response(404, 'Cat not found')
class Cat(Resource):
    @capi.doc('get_cat')
    @capi.marshal_with(cat)
    def get(self, id):
        '''Fetch a cat given its identifier'''
        for cat in CATS:
            if cat['id'] == id:
                return cat
        capi.abort(404)


api.add_namespace(capi, path='/cat')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5015, debug=True)