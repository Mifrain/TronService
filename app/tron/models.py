from sqlalchemy import Column, Integer, String, Float, DateTime
from app.database import Base


class TronInfo(Base):
    __tablename__ = 'troninfo'

    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=False)
    balance_trx = Column(Float, nullable=False)
    bandwidth = Column(Integer, nullable=False)
    energy = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)
