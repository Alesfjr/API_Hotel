from flask_restful import Resource,reqparse
from models.hotel import HotelModel


hoteis = [
        {
        'hotel_id':'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria':299.99,
        'cidade':'Rio de Janeiro'
        },
        {
        'hotel_id':'bravo',
        'nome': 'Bravo Hotel',
        'estrelas': 4.6,
        'diaria':359.99,
        'cidade':'São Paulo'
        },
        {
        'hotel_id':'charlie',
        'nome': 'Charlie Hotel',
        'estrelas': 4.8,
        'diaria':599.99,
        'cidade':'Paris'
        }
]


class Hoteis (Resource):
    def get (self):
        return {'Hoteis': hoteis}
    
class Hotel (Resource):
    
    argumentos= reqparse.RequestParser()
    argumentos.add_argument( 'nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')  
    
    def find_hotel(hotel_id):
         
        for hotel in hoteis:
            
            if hotel['hotel_id'] == hotel_id:
                return hotel
            
        return None
         
    def get (self, hotel_id):
        
        hotel = Hotel.find_hotel(hotel_id)
        
        if hotel :
            return hotel
        
        return{'message': 'Hotel not found'},404# not found
            
    def post (self, hotel_id):
        

        dados= Hotel.argumentos.parse_args()
        hotel_objeto=HotelModel(hotel_id, **dados)
        novo_hotel=hotel_objeto.json()
        hoteis.append(novo_hotel)
        return novo_hotel , 200 #OK
    
    
    def put (self, hotel_id):
         
        dados = Hotel.argumentos.parse_args() 
         #aplicando a classe HotelModel 
        hotel_objeto=HotelModel(hotel_id, **dados)
        novo_hotel=hotel_objeto.json()
        hoteis.append(novo_hotel) 
        hotel = Hotel.find_hotel(hotel_id)
        
        if hotel: 
            
            hotel.update(novo_hotel)
            return novo_hotel, 200 #OK
        
        hoteis.append(novo_hotel)
        return novo_hotel , 201 #create 
    
    def delete (self, hotel_id):
        
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message':'Hotel Deleted'}
        
        
    