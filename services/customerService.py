from database import db #services interact directly with the db
from flask import request, jsonify
from models.customer import Customer #need this to create customer objects
from models.product import Product
from models.order import Order
from sqlalchemy import select #so we can query our db
from utils.util import encode_token
from models.customerCart import customer_cart #need this to create cart objects
from models.orderProduct import order_product
import datetime
from datetime import date

def save(customer_data):

    new_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'], username=customer_data['username'], password=customer_data['password'])
    db.session.add(new_customer)
    db.session.commit() #adding our new customer to our db

    db.session.refresh(new_customer)
    return new_customer


def find_all():
    query = select(Customer)
    all_customers = db.session.execute(query).scalars().all()

    return all_customers


def login(credentials):
    query = select(Customer).where(Customer.email == credentials['email'])
    customer = db.session.execute(query).scalar_one_or_none()

    if customer and customer.password == credentials['password']: #if there is a customer, check their password
        auth_token = encode_token(customer.id)
        return auth_token
    
    return None


def add_to_cart(customer_data):

    product = db.session.get(Product, customer_data['product_id'])
    customer = db.session.get(Customer, customer_data['customer_id'])
    if not product or not customer:
        return None
    
    else:
        customer.customer_cart.append(product)
        db.session.add(customer)
        db.session.commit()

        return 'success'
    



def view_cart(customer_id):
    # Query the customer and their cart
    customer = db.session.query(Customer).filter_by(id=customer_id).first()
    
    if not customer or not customer.customer_cart:
        return None

    # The customer_cart should contain a list of Product objects
    cart_items = []
    for product in customer.customer_cart:
        cart_items.append({
            "product_id": product.id,
            "name": product.name,
            "price": product.price
        })
    
    # Return customer data along with products in the cart
    return {
        "customer_id": customer.id,
        "products": cart_items
    }



def remove_from_cart(customer_id, product_id):
    # Query the customer and the product
    customer = db.session.query(Customer).filter_by(id=customer_id).first()
    product = db.session.query(Product).filter_by(id=product_id).first()

    if not customer:
        return {"error": "Customer not found"}, 404

    if not product:
        return {"error": "Product not found"}, 404

    # Check if the product is in the customer's cart
    if product not in customer.customer_cart:
        return {"error": "Product not found in cart"}, 400

    # Remove the product from the cart
    customer.customer_cart.remove(product)

    # Commit the changes to the database
    db.session.commit()

    return {"message": f"Product {product.name} removed from cart"}, 200


def empty_cart(customer_id):
    # Query the customer
    customer = db.session.query(Customer).filter_by(id=customer_id).first()

    if not customer:
        return {"error": "Customer not found"}, 404

    # Clear the customer's cart
    customer.customer_cart = []

    # Commit the changes to the database
    db.session.commit()

    return {"message": "Cart has been emptied"}, 200




def place_order(customer_id):
    # Query the customer
    customer = db.session.query(Customer).filter_by(id=customer_id).first()

    if not customer:
        return {"error": "Customer not found"}, 404

    # Create a new order
    new_order = Order(customer_id=customer_id, order_date=date.today())
    db.session.add(new_order)
    db.session.flush()  # Get the new order's ID

    # Add items from the cart to the new order
    for product in customer.customer_cart:
        db.session.execute(order_product.insert().values(
            order_id=new_order.id,
            product_id=product.id
        ))

    # Clear the customer's cart
    customer.customer_cart = []

    # Commit the changes to the database
    db.session.commit()

    return {"message": "Order created your cart is empty"}, 200

