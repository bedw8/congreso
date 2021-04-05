#! /usr/bin/python

'''
Este codigo descarga la lista de las votaciones realizadas durante los años 2018,2019 y 2020. La lista se guarda en formato CSV
'''


import pandas as pd
import requests as re
import xmltodict

url_base = 'http://opendata.camara.cl/camaradiputados/WServices/WSLegislativo.asmx/retornarVotacionesXAnno?prmAnno='

res18 = re.get(url_base+'2018')
res19 = re.get(url_base+'2019')
res20 = re.get(url_base+'2020')

lista_v = [r.text for r in [res18,res19,res20]]

def parse_votacion(xml):
    xmlDict = xmltodict.parse(xml)

    data = []
    for i, votacion in enumerate(xmlDict['VotacionesColeccion']['Votacion']):
        # Columnas
        if i == 0:
            cols = [key for key in votacion]

        data.append([votacion[d] for d in votacion])

    df = pd.DataFrame(data)  # Pasamos a DataFrame.
    df.columns = cols  # Cargamos el nombre de las columnas.
    df.Fecha = pd.to_datetime(df.Fecha).dt.date # Dejamos solo la fecha. Sin hora.
    df.Id = pd.to_numeric(df.Id)
    # separamos texto de codigos numericos
    df[['Tipo','TipoCode']] = df.apply(lambda row : text_valor(row,'Tipo'),axis=1,result_type='expand')
    df[['Resultado','ResultadoCode']] = df.apply(lambda row : text_valor(row,'Resultado'),axis=1,result_type='expand')
    df[['Quorum','QuorumCode']] = df.apply(lambda row : text_valor(row,'Quorum'),axis=1,result_type='expand')
    return df

def text_valor(x,string):
    try:
        return [x[string]['#text'],x[string]['@Valor']]
    except:
        return [ None,None ]

lista_df = [parse_votacion(i) for i in lista_v]

df = pd.concat(lista_df).sort_values('Id')

pvix = df[df['Id']==28231].index[0] # index primera votación periodo 
df = df[pvix:]

df.to_csv('CSV/lista.csv',index=False)
