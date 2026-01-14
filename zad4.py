import pandas as pd

data={
    "nr.id": [1, 2, 3, 4, 5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Stanowisko': ['Manager', 'Programista', 'Konsultant', 'Programista', 'Manager'],
    'Wiek': [35, 28, 40, 30, 45],
    'Pensja': [8000, 4500, 6000, 5500, 7000]
}
df=pd.DataFrame(data)

prac_5000=df[df['Pensja']>5000]
df_posortowane = df.sort_values(by='Wiek', ascending=True)
groups=df.groupby("Stanowisko")["Pensja"].mean()

nowe_stanowisko_data={
    "nr.id": [2, 4],
    "Stanowisko": ["Senior Manager", "Senior Programista"],
}
promocje=pd.DataFrame(nowe_stanowisko_data)
df_merged=pd.merge(df, promocje, on="nr.id", how="left")

df.to_csv('pracownicy.csv', index=False, encoding='utf-8')
df_loaded = pd.read_csv('pracownicy.csv')
print("--- a ---")
print(prac_5000)
print("\n--- b ---")
print(df_posortowane)
print("\n--- c ---")
print(groups)
print("\n--- d ---")
print(df_merged)
print("\n--- f ---")
print(df_loaded.head())