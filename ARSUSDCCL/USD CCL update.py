#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 18:35:00 2019

@author: lucasgday
"""

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

#Traigo la última tabla para ver cuál fue la última fecha de actualización, y borro la última fecha de la tabla por si está actualizada a mitad del día

tabla_a_actualizar=pd.DataFrame(pd.read_csv('dolar_2019.csv'))
tabla_a_actualizar=tabla_a_actualizar.set_index('Date')
ultima_fecha=tabla_a_actualizar.tail(1).index.values[0][:10]
tabla_a_actualizar=tabla_a_actualizar.iloc[:-1]

#Creo un nuevo df a partir de la última fecha, trayendo Galicia $ y US$ para calcular el CCL, y el TC Oficial

tickers=['GGAL.BA','GGAL',"ARS=X"]
new_data=pd.DataFrame(columns=tickers)

for ticker in tickers:
    new_data[ticker]=yf.download(ticker,start=ultima_fecha)['Adj Close']

#Calculo el CCL y creo nuevo DF para actualizar la tabla antigua
new_data['CCL']=new_data['GGAL.BA']/new_data['GGAL']*10
tabla_a_anexar=new_data[['ARS=X',"CCL"]]
tabla_a_anexar.columns=['Oficial','CCL']

#Agrego la nueva data a la tabla a actualizar y la guardo de nuevo en el csv

tabla_a_actualizar=tabla_a_actualizar.append(tabla_a_anexar)
tabla_a_actualizar['CCL'].interpolate(method='linear',inplace=True)

print(tabla_a_actualizar.head())
print(tabla_a_actualizar.tail())

tabla_a_actualizar.plot()
plt.show()

tabla_a_actualizar.to_csv('dolar_2019.csv') 