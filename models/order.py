from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
import datetime
from typing import List
from models.orderProduct import order_product

class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True) #primary keys auto increment
    order_date: Mapped[datetime.date] = mapped_column(db.Date, nullable= False)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('customers.id'))
    customer: Mapped['Customer'] = db.relationship(back_populates="orders")
    products: Mapped[List['Product']] = db.relationship(secondary=order_product)