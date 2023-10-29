# B"H

from sqlalchemy import Column, String, Integer, ForeignKey, Table, Float, DateTime
from sqlalchemy.orm import relationship, backref
from base import Base

class HourlyProduction(Base):
    __tablename__ = 'hourly_production'
    id = Column(Integer(), primary_key=True)

    time_date = Column(DateTime()) 
    time_hour = Column(Integer())

    power_plant_id = Column(Integer(), ForeignKey('power_plant.id'))
    power_plant = relationship("PowerPlant", backref=backref("hourly_production"))

    gen_mwh = Column(Float())

    def __init__(self
    , time_date
    , time_hour
    , power_plant
    , gen_mwh
    ):

        self.time_date = time_date
        self.time_hour = time_hour
        self.power_plant = power_plant
        self.gen_mwh = gen_mwh
        
