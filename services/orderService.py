from database import db #services interact directly with the db
from models.order import Order #need this to create order objects
from sqlalchemy import select 
from models.product import Product
from datetime import date


def save(order_data):

    new_order = Order(customer_id=order_data['customer_id'], order_date=date.today())

    for item_id in order_data['product_ids']:
        query = select(Product).where(Product.id==item_id) #search the product table for a product whose id is the same as the item_id we are looping over
        item = db.session.execute(query).scalar()
        new_order.products.append(item) #creates the connection from Order to the associate id, and populates our order_product table
    
    db.session.add(new_order)
    db.session.commit() #adding our new order to our db

    db.session.refresh(new_order)
    return new_order


def find_all():
    query = select(Order)
    all_orders = db.session.execute(query).scalars().all()

    return all_orders