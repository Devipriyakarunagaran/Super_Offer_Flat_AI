from sqlalchemy import Column, Integer, String, Float
from database import Base

class Offer(Base):

    __tablename__ = "offers"

    id = Column(Integer, primary_key=True, index=True)

    product = Column(String)
    store = Column(String)
    price = Column(Float)
