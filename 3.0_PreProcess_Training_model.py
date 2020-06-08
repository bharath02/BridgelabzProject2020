import pandas as pd
import numpy as np
data=pd.read_csv('HistoricalQuotes.csv')
print(data.size)
print(data.head())
print(data.isnull().count())
print(data.info())
print(data.dtypes)

pd.to_datetime(data['Date'])
data['Close/Last'].astype(str).astype(int)
data['Open'].astype(str).astype(int)
data['High'].astype(str).astype(int)
data['Low'].astype(str).astype(int)

print(data.dtypes)