import pandas as pd

f = pd.read_csv("n26.csv")

keep_columns = ['Date','Payee','Payment reference','Amount (EUR)']
f2 = f[keep_columns]
f3 = f2.rename(columns = {'Payment reference': 'Memo', 'Amount (EUR)': 'Amount'})
f3.to_csv("new.csv", index=False)
