from flask import Blueprint
from controllers.customerController import save, find_all, login, add_to_cart, view_cart, remove_item_from_cart, empty_cart, place_order


customer_blueprint = Blueprint('customer_bp', __name__)

#url_prefix for this blueprint is /customers

customer_blueprint.route('/create', methods=['POST'])(save) #triggers the save function on POST request to /customers/create
customer_blueprint.route('/', methods=['GET'])(find_all) #triggers the findall function on GET request to /customers
customer_blueprint.route('/login', methods=["POST"])(login)
customer_blueprint.route('/cart/add', methods=['POST'])(add_to_cart)
customer_blueprint.route('/cart/view', methods=['GET'])(view_cart)
customer_blueprint.route('/cart/remove', methods=['POST'])(remove_item_from_cart)
customer_blueprint.route('/cart/empty', methods=['POST'])(empty_cart)
customer_blueprint.route('/order/place', methods=['POST'])(place_order)

