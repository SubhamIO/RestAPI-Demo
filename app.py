#!flask/bin/python
import os
import sys
print("===app.py ----- PATH===", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(""+os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask, make_response
from flask_restful import Resource, Api
from resources.Square import Square

#import config
from simplexml import dumps
import json

def output_xml(data, code, headers=None):
    """Makes a Flask response with a XML encoded body"""
    resp = make_response(dumps({'response' :data}), code)
    resp.headers.extend(headers or {})
    return resp



# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app, default_mediatype='application/json')
api.representations['application/xml'] = output_xml
# adding the defined resources along with their corresponding urls
api.add_resource(Square, '/square/<int:num>') # 'num' variable was passed as argument in get function in Square.py


# Load the default configuration
#app.config.from_object(config)



# driver function
if __name__ == '__main__':
    app.run(debug = True)

'''Run in browser using  :  http://127.0.0.1:5000/square/8'''
