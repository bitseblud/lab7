import pandas as pd

data = {
    'Nr_albumu': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał', 'Piotr', 'Maria', 'Adam', 'Ewa', 'Jakub'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński', 'Lewandowski', 'Wójcik', 'Mazur', 'Krawczyk', 'Stępień'],
    'Ocena': [4.5, 3.0, 5.0, 4.0, 2.5, 4.5, 3.0, 4.0, 5.0, 3.0],
    'WiekS': [22, 21, 24, 23, 25, 22, 20, 22, 23, 21]
}

df = pd.DataFrame(data)

ocena4 = df[df['Ocena'] > 4]
sorted_df = df.sort_values(by='WiekS')
grupy = df.groupby('Ocena')['WiekS'].mean()

data_poprawa = {
    'Nr_albumu': [2, 5, 10],
    'Ocena_poprawa': [4.0, 3.5, 4.5]
}

df_poprawa = pd.DataFrame(data_poprawa)
df_merged = pd.merge(df, df_poprawa, on='Nr_albumu', how='left')

df.to_csv('studenci.csv', index=False)
df_read = pd.read_csv('studenci.csv')

nowak = {'Nr_albumu': 11, 'Imię': 'Zofia', 'Nazwisko': 'Szymańska', 'Ocena': 4.5, 'WiekS': 24}
df = pd.concat([df, pd.DataFrame([nowak])], ignore_index=True)

unique_grades = df['Ocena'].unique()
count_grade_5 = (df['Ocena'] == 5.0).sum()

print(grupy)
print(f"Liczba ocen 5.0: {count_grade_5}")