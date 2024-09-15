from database import db, Base

customer_cart = db.Table(
    'Customer_Cart',
    Base.metadata,
    db.Column('customer_id', db.ForeignKey('customers.id')),
    db.Column('product_id', db.ForeignKey('products.id'))
)