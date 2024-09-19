from flask import Blueprint
from controllers.productController import save, find_all


product_blueprint = Blueprint('product_bp', __name__)

#url_prefix for this blueprint is /products

product_blueprint.route('/create', methods=['POST'])(save) #triggers the save function on POST request to /products/create
product_blueprint.route('/', methods=['GET'])(find_all) #triggers the findall function on GET request to /products
