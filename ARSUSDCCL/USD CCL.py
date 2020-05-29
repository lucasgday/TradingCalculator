#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 18:35:00 2019

@author: lucasgday
"""

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

tickers=['GGAL.BA','GGAL',"ARS=X"]
anual=pd.DataFrame(columns=tickers)

for ticker in tickers:
    anual[ticker]=yf.download(ticker,start='2019-01-01')['Adj Close']

anual['CCL']=anual['GGAL.BA']/anual['GGAL']*10
dolar=pd.DataFrame(columns=['Oficial','CCL'])
dolar['Oficial']=anual["ARS=X"]
dolar['CCL']=anual['CCL']
dolar['CCL'].interpolate(method='linear',inplace=True)
print(dolar.head())

dolar.plot()
plt.show()

dolar.to_csv('dolar_2019.csv')