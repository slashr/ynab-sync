import pandas as pd

f = pd.read_csv("n26.csv")

keep_col = ['Date','Payee','Payment reference','Amount (EUR)']
new_f = f[keep_col]
new_f.to_csv("new.csv", index=False)
