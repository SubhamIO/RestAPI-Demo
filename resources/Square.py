from flask import jsonify
from flask_restful import Resource

class Square(Resource):

    def __init__(self):
        print("\n===================__init__==Square ==============")

    def get(self, num):
        print("\n==================get request method===Square ==============", str(num))
        return {'square': num**2}

    # Corresponds to POST request
    def post(self):

        data = request.get_json()     # status code 
        return jsonify({'data': data}), 201
