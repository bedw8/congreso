#! /usr/bin/python

'''
Este script descarga el detalle de todas las votaciones y lo guarda en formato CSV. Requiere como entrada la lista de votaciones
'''

import pandas as pd
import requests as r
import xmltodict
from os import path
from glob import glob

def parse_votacion(id):
    '''
    Se el entrega un id de votación y devuelve un DataFrame con el detalle de la votación.
    '''
    # Descargamos detalle de una Votacion a partir del id
    response = r.get('http://opendata.camara.cl/camaradiputados/WServices/WSLegislativo.asmx/retornarVotacionDetalle?prmVotacionId='+str(id))
    xmlDict = xmltodict.parse(response.text)  # Formateamos el xml

    data = []

    for child in xmlDict['Votacion']['Votos']['Voto']:
        # Definimos variable que queremos guardar
        diputado = child['Diputado']
        id = int(diputado['Id'])
        nombre = diputado['Nombre']
        ap = diputado['ApellidoPaterno']
        am = diputado['ApellidoMaterno']
        full_name = ' '.join([nombre,ap,am])
        voto = child['OpcionVoto']['#text']
        voto_cod  = int(child['OpcionVoto']['@Valor'])
        # Guardamos cada fila
        data.append([id,voto_cod,nombre,ap,am,full_name,voto])

    # Pasamos la lista a DataFrame
    df = pd.DataFrame(data)
    cols = ['Id','VotoCode','Nombre','ApellidoPaterno','ApellidoMaterno','NombreCompleto','Voto']
    df.columns = cols
    return df

def parseAll(start_id=None):
    lista_id = pd.read_csv('CSV/lista.csv')['Id']

    if start_id != None:
        sid_index = lista_id[lista_id==start_id].index[0]
        lista_id  = lista_id[sid_index:]

    for id in lista_id:
        try:
            df = parse_votacion(id)
            df.to_csv('CSV/DetalleVotaciones/'+str(id)+'.csv',index=False)
            print('La votación de id '+str(id)+' ha sido guardada')
        except:
            pass


if __name__ == '__main__':
    path = sorted(glob('CSV/DetalleVotaciones/*'))
    try:
        uvix = path[-1].split('/')[-1].split('.')[0]
        # print(path)
        print('El detalle de las votaciones ya ha sido descargado')
        print('La última votación descargada es la de id '+str(uvix))
    except:
        parseAll()
