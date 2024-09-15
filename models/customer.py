from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from models.customerCart import customer_cart

class Customer(Base):
    __tablename__ = 'customers'

    id: Mapped[int] = mapped_column(primary_key=True) #primary keys auto increment
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(db.String(255), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(db.String(25), nullable=False)
    username: Mapped[str] = mapped_column(db.String(30), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)
    orders: Mapped[List['Order']] = db.relationship(back_populates='customer')
    customer_cart: Mapped[List['Product']] = db.relationship(secondary=customer_cart)