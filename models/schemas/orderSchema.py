from . import ma
from marshmallow import fields

class orderSchema(ma.Schema): #Inherting our instance of Marshmallow 
    id = fields.Integer(required=False) #This will be auto-incremented
    order_date = fields.String(required=True)
    customer_id = fields.Float(required= True)

    class Meta:
        fields = ("id", "order_date", "customer_id") #all fields that could be coming in and going out when validating data

order_schema = OrderSchema() #instantiate a single order schema
orders_schema = OrderSchema(many=True)