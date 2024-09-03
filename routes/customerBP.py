from flask import Blueprint
from controllers.customerController import save, find_all


customer_blueprint = Blueprint('customer_bp', __name__)

#url_prefix for this blueprint is /customers

customer_blueprint.route('/customers', methods=['POST'])(save) #triggers the save function on POST request to /customers
customer_blueprint.route('/customers', methods=['GET'])(find_all)
