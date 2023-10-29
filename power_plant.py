# B"H

from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from base import Base

class PowerPlant(Base):
    __tablename__ = 'power_plant'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String(100))
    
    power_plant_type_id = Column(Integer, ForeignKey('power_plant_type.id'))
    power_plant_type = relationship("PowerPlantType", backref=backref("power_plant"))

    busbar_id = Column(Integer, ForeignKey('busbar.id'))
    busbar = relationship("Busbar", backref=backref("power_plant"))

    def __init__(self, name, power_plant_type, busbar):
        self.name = name
        self.power_plant_type = power_plant_type 
        self.busbar = busbar 

