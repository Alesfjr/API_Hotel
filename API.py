from flask import Flask
from flask_restful import  Api
from resource.hotel import Hoteis,Hotel
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
api = Api (app)



api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel,'/hoteis/<string:hotel_id>')

if __name__ == '__main__':
    app.run(debug=True)

#http://127.0.0.1:5000/hoteis#