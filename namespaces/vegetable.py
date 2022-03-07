from flask_restx import Namespace, Resource
import random 

api = Namespace('vegetables', description='Vegetables-related operations')


vegs = ['Carrot', 'Egg plant']


@api.route('/')
class VegGen(Resource):
    @api.doc('Returns a vegetable')
    def get(self):
        '''Returns random vegetable'''
        return {'veg': random.choice(vegs)}
