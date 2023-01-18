import pandas as pd
import os

f = pd.read_csv("/Users/primus/Downloads/n26-csv-transactions.csv")

keep_columns = ['Date','Payee','Payment reference','Amount (EUR)']
f2 = f[keep_columns]
f3 = f2.rename(columns = {'Payment reference': 'Memo', 'Amount (EUR)': 'Amount'})
f3.to_csv("new.csv", date_format='%Y%m%d')

os.remove("/Users/primus/Downloads/n26-csv-transactions.csv") 
