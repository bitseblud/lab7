import pandas as pd
df = pd.read_csv('demografia.csv', na_values=['0'], decimal='.')
df_numeric = df.drop(columns=['KRAJE'])
df_numeric = df_numeric.apply(pd.to_numeric, errors='coerce')
max_przyrost = df_numeric.max()
rok_z_maksimum = max_przyrost.idxmax()
indeks_wiersza = df_numeric[rok_z_maksimum].idxmax()
kraj = df.loc[indeks_wiersza, 'KRAJE']

print(f"Największy przyrost wystąpił w roku: {rok_z_maksimum}")
print(f"Kraj, którego dotyczy ten przyrost: {kraj}")
print(f"Wartość przyrostu: {df_numeric.loc[indeks_wiersza, rok_z_maksimum]}")