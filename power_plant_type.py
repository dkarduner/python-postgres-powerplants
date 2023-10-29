# B"H 

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class PowerPlantType(Base):
    __tablename__ = 'power_plant_type'
   
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), unique=True)
 
    def __init__(self, name):
        self.name = name 
