from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

class Product(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True) #primary keys auto increment
    order_date: Mapped[date] = mapped_column(db.Date, nullable= False)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('customer.id'))