from flask import request, jsonify
from models.schemas.productSchema import product_schema, products_schema
from services import productService
from marshmallow import ValidationError


def save(): #name the controller the same as the service it recruites

    try:
        product_data = product_schema.load(request.json)
    
    except ValidationError as e:
        return jsonify(e.messages), 400 #return error message with a 400 failed response
    
    new_product = productService.save(product_data)
    return product_schema.jsonify(new_product), 201 #send them the product object with a 201 successful creation status


def find_all():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 2, type=int)
    all_products = productService.find_all(page, per_page)

    return products_schema.jsonify(all_products), 200