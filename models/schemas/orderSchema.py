from . import ma
from marshmallow import fields

#incoming order data
'''
{
    "customer_id": int,
    "product_ids": [ints] list of product ids that will be used to create the relationship from this order to all the products
}
'''

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False) 
    order_date = fields.String(required=True)
    customer_id = fields.Float(required= True)
    products = fields.Nested("ProductSchema", many=True)


    class Meta:
        fields = ("id", "order_date", "customer_id", "product_ids", "products") #all fields that could be coming in and going out when validating data

order_schema = OrderSchema() #instantiate a single order schema
orders_schema = OrderSchema(many=True)