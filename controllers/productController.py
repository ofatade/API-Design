from flask import request, jsonify
from models.schemas.productSchema import product_schema, products_schema
from services import productService
from marshmallow import ValidationError
from cache import cache


def save(): #name the controller the same as the service it recruites

    try:
        product_data = product_schema.load(request.json)
    
    except ValidationError as e:
        return jsonify(e.messages), 400 #return error message with a 400 failed response
    
    product = productService.save(product_data)
    return product_schema.jsonify(product), 201 #send them the product object with a 201 successful creation status


@cache.cached(timeout=120)
def find_all():
    all_products = productService.find_all()

    return products_schema.jsonify(all_products), 200