import uuid
from sqlalchemy import Column, ForeignKey, Numeric, Boolean, DateTime
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base

class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(UNIQUEIDENTIFIER, primary_key=True, default=uuid.uuid4)
    client_id = Column(UNIQUEIDENTIFIER, ForeignKey("clients.id"), nullable=False, unique=True)
    balance = Column(Numeric(10, 2), default=0.0, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now)
    
    client = relationship("Client", back_populates="wallet")
    history_matches = relationship("HistoryMatch", back_populates="wallet")
    transactions = relationship("Transaction", back_populates="wallet")
