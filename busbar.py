# B"H

from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from base import Base

class Busbar(Base):
    __tablename__ = 'busbar'
   
    id = Column(Integer(), primary_key=True)
    name = Column(String(100))
 
    def __init__(self, name):
        self.name = name 
