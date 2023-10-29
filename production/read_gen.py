# B"H

import csv

with open("2023-8.tsv") as file:
    tsv_file = csv.reader(file, delimiter="\t")
    for line in tsv_file:    
        if line[3] == "HP MAITENES":
            print(line)

        '''
        fecha_opreal
        hora_opreal
        central_infotecnica_id
        central_nombre
        central_tipo
        central_tipo_nemotecnico
        generacion_real_mwh 
        generacion_real_ernc_mwh  
'''
