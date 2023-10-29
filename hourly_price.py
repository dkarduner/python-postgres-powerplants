# B"H

from sqlalchemy import Column, String, Integer, ForeignKey, Table, Float, DateTime
from sqlalchemy.orm import relationship, backref
from base import Base

class HourlyPrice(Base):
    __tablename__ = 'hourly_price'
    id = Column(Integer(), primary_key=True)

    time_date = Column(DateTime()) 
    time_hour = Column(Integer())
    
    busbar_id = Column(Integer(), ForeignKey('busbar.id'))
    busbar = relationship("Busbar", backref=backref("hourly_price"))
    
    price_usd_mwh = Column(Float())

    def __init__(self
    , time_date
    , time_hour 
    , busbar 
    , price_usd_mwh
    ):

        self.time_date = time_date 
        self.time_hour = time_hour 
        self.busbar = busbar 
        self.price_usd_mwh = price_usd_mwh 
        
