from . import ma
from marshmallow import fields

#incoming customer_cart data
'''
{
    "customer_id": int,
    "product_ids": [ints] list of product ids that will be used to create the relationship from this order to all the products
}
'''

class Customer_CartSchema(ma.Schema):
    id = fields.Integer(required=False) 
    customer_id = fields.Float(required= True)
    products = fields.Nested("ProductSchema", many=True)


    class Meta:
        fields = ("id", "customer_id", "product_ids", "products") #all fields that could be coming in and going out when validating data

customer_cart_schema = Customer_CartSchema() #instantiate a single customer_cart schema
customer_carts_schema_schema = Customer_CartSchema(many=True)