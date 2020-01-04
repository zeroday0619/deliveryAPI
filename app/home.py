from flask import Flask
from flask_restful import Resource
from flask_restful import reqparse
from app.carriers.de_dhl import de_dhl

class DHL_API(Resource):
    def post(self):
        try:
            pasrser = reqparse.RequestParser()
            pasrser.add_argument('track_id', type=str)

            args = pasrser.parse_args()
            _track_id = args['track_id']
            print(_track_id)
            da = de_dhl().query(track_id=args['track_id'])
            return {'tracking' : [da]}
        except Exception as e:
            return {'error': str(e)}

