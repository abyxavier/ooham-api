from app.core.database import Base
from sqlalchemy import Column,Integer,String,TIMESTAMP,ForeignKey,Text,JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    email=Column(String(255),unique=True,nullable=False)
    name=Column(String(100))
    created_at=Column(TIMESTAMP(timezone=True),server_default=func.now())
    requests=relationship("EstimateRequest",back_populates="user",cascade="all,delete-orphan")
   
class EstimateRequest(Base):
    __tablename__="estimate_request" 
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    project_description = Column(Text, nullable=False)
    seniority = Column(String(20))
    deadline_preference = Column(String(20))
    budget = Column(String(100))
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="requests")
    result = relationship("EstimationResult", back_populates="request", uselist=False)
    
class EstimationResult(Base):
    __tablename__ = "estimation_results"

    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(Integer, ForeignKey("estimate_request.id"))
    estimated_time = Column(String(100))
    estimated_cost = Column(String(100))
    team = Column(JSON)
    risks = Column(JSON)
    architecture = Column(JSON)
    task_breakdown = Column(JSON)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    request = relationship("EstimationRequest", back_populates="result")
    