from database import db #services interact directly with the db
from models.order import Order #need this to create order objects
from sqlalchemy import select #so we can query our db


def save(order_data):

    new_order = Order(order_date=order_data['order_date'], customer_id=order_data['customer_id'])
    db.session.add(new_order)
    db.session.commit() #adding our new order to our db

    db.session.refresh(new_order)
    return new_order


def find_all():
    query = select(Order)
    all_orders = db.session.execute(query).scalars().all()

    return all_orders