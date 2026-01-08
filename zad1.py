import pandas as pd
df=pd.read_csv('demografia.csv', na_values=['0'],decimal='.')
print(df)