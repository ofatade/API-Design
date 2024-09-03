from flask import request, jsonify
from models.schemas.orderSchema import order_schema, orders_schema
from services import orderService
from marshmallow import ValidationError
from cache import cache


def save(): #name the controller the same as the service it recruites

    try:
        order_data = order_schema.load(request.json)
    
    except ValidationError as e:
        return jsonify(e.messages), 400 #return error message with a 400 failed response
    
    order = orderService.save(order_data)
    return order_schema.jsonify(order), 201 #send them the customer object with a 201 successful creation status


@cache.cached(timeout=120)
def find_all():
    all_orders = orderService.find_all()

    return orders_schema.jsonify(all_orders), 200