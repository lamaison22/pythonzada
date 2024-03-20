from flask_restful import Resource, reqparse
from models.hotel import HotelModel
hoteis=[
    {
        'hotel_id':'alpha',
        'nome': 'alpha hotel',
        'estrelas': '4.4',
        'diaria':'420.34',
        'cidade':'salam'
    },
     {
        'hotel_id':'beta',
        'nome': 'beta hotel',
        'estrelas': '4.2',
        'diaria':'322.34',
        'cidade':'chapeco'
        
    },
      {
        'hotel_id':'treta',
        'nome': 'treta hotel',
        'estrelas': '3.4',
        'diaria':'122.34',
        'cidade':'rollalndia'
        
    }
    ]




class Hoteis (Resource):
    def get(self):
        return {'hoteis': hoteis}
    
class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
        
    def findHotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id']==hotel_id:
                return hotel
        return None
        
    def get(self,hotel_id):
        hotel=Hotel.findHotel(hotel_id)
        if(hotel):
            return hotel
        return {'message':' Hotel not found'},404
    def post (self,hotel_id):
       
        dados=Hotel.argumentos.parse_args()
        hotel_objeto=HotelModel(hotel_id,**dados)
        novo_hotel=hotel_objeto.json()
            
        hoteis.append(novo_hotel)
        return novo_hotel,200
        
        
        
        
    def put (self,hotel_id):
        dados=Hotel.argumentos.parse_args()
        hotel_objeto=HotelModel(hotel_id,**dados)
        novo_hotel=hotel_objeto.json()
        hotel=Hotel.findHotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel,200
        hoteis.append(novo_hotel)
        return novo_hotel,201 #criado
    
    def delete(self,hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id']!=hotel_id]
        return {'message': 'Hotel deleted'}