# B"H

import csv, os 
import pandas as pd
from datetime import date
from pathlib import Path

from power_plant_type import PowerPlantType
from busbar import Busbar 
from power_plant import PowerPlant
from hourly_production import HourlyProduction
from hourly_price import HourlyPrice
from timestamp import Timestamp 

import numpy as np
from psycopg2.extensions import register_adapter, AsIs
register_adapter(np.int64, AsIs)

from base import Session, engine, Base

if __name__ == '__main__':
    # generate database schema
    Base.metadata.create_all(engine)
    # create a new session for adding data
    session = Session()

    # power_plants.csv data 
    with open('power_plants.csv') as file:
        readlines = csv.reader(file)
        next(readlines)
        for line in readlines:
            _power_plant_type_name = line[1]
            _power_plant_type = PowerPlantType(_power_plant_type_name)
            session.add(_power_plant_type)
            
            # extracting info from busbar
            _busbar_name = line[2]
            _busbar = Busbar(_busbar_name)
            session.add(_busbar)
           
            # adding busbar prices
            _files = [f for f in os.listdir('./prices') if f.endswith('.tsv')]
            for f in _files:
                file_path = os.path.join(Path.cwd(), 'prices/', f)
                with open(file_path) as file:
                    df = pd.read_table(file)
                    df = df[df['nombre']==_busbar_name]
                    df.fillna("")
                    for i in range(len(df)):
                        time_date = df.iloc[i, 2]
                        time_hour = df.iloc[i, 3]
                        price_usd_mwh = float(str(df.iloc[i, 4]).replace(',','.'))
                        _hourly_price = HourlyPrice(time_date, time_hour, _busbar, price_usd_mwh)
                        session.add(_hourly_price)


            # extracting info from power_plant
            _power_plant_name = line[0]
            _power_plant = PowerPlant(_power_plant_name, _power_plant_type, _busbar)
            session.add(_power_plant)
               
            # adding info from production using _power_plant relation
            _files = [f for f in os.listdir('./production') if f.endswith('.tsv')]
            for f in _files:
                file_path = os.path.join(Path.cwd(), 'production/', f)
                with open(file_path) as file:
                    df = pd.read_table(file)
                    df = df[df['central_nombre']==_power_plant_name]
                    df.fillna("")
                                        
                    for i in range(len(df)):
                        time_date = df.iloc[i, 0]
                        time_hour = df.iloc[i, 1]
                        gen_mwh = df.iloc[i, 6]
                        _hourly_production = HourlyProduction(time_date, time_hour, _power_plant, gen_mwh)
                        session.add(_hourly_production)


    # commit and close session
    session.commit()
    session.close()
'''
                    readlines = csv.reader(file, delimiter="\t")
                    next(readlines)
                    for line in readlines:
                        time_date = line[0]
                        time_hour = line[1]
                        power_plant = line[3]
                        power_plant_type = line[5]
                        gen_mwh = line[6]

                        _hourly_production = HourlyProduction( 
                        time_date
                        , time_hour
                        , power_plant
                        , power_plant_type
                        , gen_mwh
                        )
                        
                        session.add(_hourly_production)
                        #print(line)
                

            _hourly_production = HourlyProduction( 
            '2023-03-01'
            , 23
            , _power_plant
            , 22.1
            )

            session.add(_hourly_production)
            #print(line)


            _power_plant_type = PowerPlantType(line[1])
            session.add(_power_plant_type)
            
            _busbar = Busbar(line[2])
            session.add(_busbar)

            _power_plant = PowerPlant(line[0], _power_plant_type, _busbar)
            session.add(_power_plant)
            #print(line)
        
    '''


        # load price data

