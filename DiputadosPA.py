#! /usr/bin/python

'''
Este script descarga datos de los diputdaos y lo guarda en formato CSV
'''

import requests as r
import xmltodict
import pandas as pd

response = r.get('http://opendata.camara.cl/camaradiputados/WServices/WSDiputado.asmx/retornarDiputadosPeriodoActual?')

xmlDict = xmltodict.parse(response.text)

data = []

for d in xmlDict['DiputadosPeriodoColeccion']['DiputadoPeriodo']:
    id = d['Diputado']['Id']
    nombre = d['Diputado']['Nombre']
    nombre2 = d['Diputado']['Nombre2']
    ap = d['Diputado']['ApellidoPaterno']
    am = d['Diputado']['ApellidoMaterno']
    try:
        nombre_full = ' '.join([nombre,nombre2,ap,am])
    except:
        nombre_full = ' '.join([nombre,ap,am])
    try:
        militancia = d['Diputado']['Militancias']['Militancia'][-1]['Partido']['Id']
    except KeyError:
        # print(d['Diputado']['Militancias']['Militancia'])
        militancia = None
    data.append([id,nombre,nombre2,ap,am,nombre_full,militancia])

df = pd.DataFrame(data)
cols = ['Id','Nombre','Nombre2','ApellidoPaterno','ApellidoMaternos','NombreCompleto','Militancia']
df.columns = cols

# print(df)
df.to_csv('CSV/diputados.csv',index=False)
