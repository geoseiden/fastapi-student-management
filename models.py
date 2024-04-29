from sqlalchemy import Column, Integer, String, Date
from database import Base

class Mentors(Base):
    __tablename__ = "mentors"
    empid = Column(String(14), primary_key=True)  
    name = Column(String(50))
    desig = Column(String(20))  
    email = Column(String(50))
    ph = Column(Integer)  
    password = Column(String(10))  

class Students(Base):
    __tablename__ = "students"
    regno = Column(String(14), primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    phone = Column(Integer)
    programme = Column(String(100))
    score = Column(Integer)
    empid = Column(String(10))