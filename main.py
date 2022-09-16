import pandas as pd

df = pd.read_excel('test.xlsx', header=None)
res = dict(zip(df[0],df[1]))
print(res)