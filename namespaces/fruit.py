from flask_restx import Namespace, Resource
import random 

api = Namespace('fruits', description='Fruits-related operations')


fruits = ['Apple', 'Banana']


@api.route('/')
class FruitGen(Resource):
    @api.doc('Returns a fruit')
    def get(self):
        '''Returns random fruit'''
        return {'fruit': random.choice(fruits)}
