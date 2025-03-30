import uuid
from sqlalchemy import Column, ForeignKey, Numeric, DateTime
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base

class HistoryMatch(Base):
    __tablename__ = "history_matches"

    id = Column(UNIQUEIDENTIFIER, primary_key=True, default=uuid.uuid4)
    client_id = Column(UNIQUEIDENTIFIER, ForeignKey("clients.id"), nullable=False)
    value_bet = Column(Numeric(10, 2), nullable=False)
    games_id = Column(UNIQUEIDENTIFIER, ForeignKey("games.id"), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now)
    
    client = relationship("Client", back_populates="history_matches")
    games = relationship("Game", back_populates="history_matches")
