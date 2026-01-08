import pandas as pd
df=pd.read_csv('demografia.csv', na_values=['0'],decimal='.')
max_przyrost=df['2022'].idxmax(skipna=True)
print(max_przyrost)
kraj=df.loc[max_przyrost, "KRAJE"]
print(kraj)
