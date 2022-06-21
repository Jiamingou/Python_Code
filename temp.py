import pandas as pd
import pandas_datareader as pdr

data = pdr.get_data_yahoo('AAPL',start='2000-01-01',end='2022-01-01')

print(data)

ok