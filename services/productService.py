from database import db #services interact directly with the db
from models.product import Product #need this to create product objects
from sqlalchemy import select #so we can query our db


def save(product_data):

    new_product = Product(name=product_data['name'], price=product_data['price'])
    db.session.add(new_product)
    db.session.commit() #adding our new product to our db

    db.session.refresh(new_product)
    return new_product


def find_all(page=1, per_page=2):
    query = select(Product)
    all_products = db.paginate(query, page=int(page), per_page=int(per_page)) #our paginated query is dependant on a page number and how many we wish to show per page

    return all_products