from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True) #primary keys auto increment
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    price: Mapped[float] = mapped_column(db.Float, nullable= False)