from . import ma
from marshmallow import fields

class ProductSchema(ma.Schema): #Inherting our instance of Marshmallow 
    id = fields.Integer(required=False) #This will be auto-incremented
    name = fields.String(required=True)
    price = fields.Float(required= True)

    class Meta:
        fields = ("id", "name", "price") #all fields that could be coming in and going out when validating data

product_schema = ProductSchema() #instantiate a single product schema
products_schema = ProductSchema(many=True)