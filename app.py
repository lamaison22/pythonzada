from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis
from resources.hotel import Hotel


app = Flask(__name__)
api = Api (app)



api.add_resource(Hoteis,'/hoteis')
api.add_resource(Hotel,'/hoteis/<string:hotel_id>')


if __name__=='__main__':
    app.run(debug=True)