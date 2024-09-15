from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema, customer_login
from models.schemas.customer_cartSchema import customer_cart_schema
from services import customerService
from marshmallow import ValidationError
from cache import cache
from utils.util import token_required


def save(): #name the controller the same as the service it recruites

    try:
        customer_data = customer_schema.load(request.json)
    
    except ValidationError as e:
        return jsonify(e.messages), 400 #return error message with a 400 failed response
    
    customer = customerService.save(customer_data)
    return customer_schema.jsonify(customer), 201 #send them the customer object with a 201 successful creation status


#@cache.cached(timeout=120)
@token_required
def find_all():
    all_customers = customerService.find_all()

    return customers_schema.jsonify(all_customers), 200


def login():
    try: 
        credentials = customer_login.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400 #invalid credential payload
    
    token = customerService.login(credentials)

    if token:
        response = {
            "status": "success",
            "message": "successfully logged in",
            "token": token
        }
        return jsonify(response), 200
    else:
        return jsonify({"status": "error", "message": "invalid username or password"}), 404
    

def add_to_cart():
    customer_data = request.json
    
    response = customerService.add_to_cart(customer_data)

    if response: 
        return jsonify({"message": "success"}), 201
    
    else:
        return jsonify({"status": "error", "message": "invalid user or product"}), 404
    


def view_cart():
    # Get customer_id from query parameters
    customer_id = request.args.get('customer_id')
    
    if not customer_id:
        return jsonify({"error": "Customer ID is required"}), 400

    # Fetch the customer's cart from the service
    cart = customerService.view_cart(customer_id)
    
    if not cart:
        return jsonify({"message": "Cart is empty"}), 200

    # Serialize the data using the schema and return a proper JSON response
    return customer_cart_schema.dump(cart), 200


def remove_item_from_cart():
    # Get customer_id and product_id from request
    customer_id = request.json.get('customer_id')
    product_id = request.json.get('product_id')

    if not customer_id or not product_id:
        return jsonify({"error": "Customer ID and Product ID are required"}), 400

    # Call the service method to remove the item
    result, status_code = customerService.remove_from_cart(customer_id, product_id)

    return jsonify(result), status_code



def empty_cart():
    # Get customer_id from request
    customer_id = request.json.get('customer_id')

    if not customer_id:
        return jsonify({"error": "Customer ID is required"}), 400

    # Call the service method to empty the cart
    result, status_code = customerService.empty_cart(customer_id)

    return jsonify(result), status_code



def place_order():
    # Get customer_id from request
    customer_id = request.json.get('customer_id')

    if not customer_id:
        return jsonify({"error": "Customer ID is required"}), 400

    # Call the service method to create the order and empty the cart
    result, status_code = customerService.place_order(customer_id)

    return jsonify(result), status_code