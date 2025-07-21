import random
import pandas as pd
import matplotlib.pyplot as plt

a = 3
b = 13
n = int(input("Introduceti numarul de valori aleatoare: "))

# Inițializare dicționar
d = {i: [0] for i in range(a, b + 1)}

# Generare și stocare valori
for i in range(n):
    val = random.randint(a, b)
    d[val][0] += 1
    d[val].append(i)

# Scriere în sample.txt
with open("sample.txt", "w") as f:
    for k, v in d.items():
        f.write(f"{k}: {v}\n")

# Pregătire date pentru analiză
counts = [v[0] for v in d.values()]
keys = list(d.keys())

# Creare DataFrame
df = pd.DataFrame({'key': keys, 'count': counts})

# Calcul statistici
mean = 0
for keys in df['key']:
    mean += keys * df[df['key'] == keys]['count'].values[0]
    
mean = mean / df['count'].sum() 
#suma de cheie*count impartit la count(i) total

median = df['count'].median()
min_val = df['count'].min()
max_val = df['count'].max()
std_dev = df['count'].std()

print(f"Media: {mean}")
print(f"Mediana: {median}")
print(f"Minim: {min_val}")
print(f"Maxim: {max_val}")
print(f"Standard deviation: {std_dev}")

# Afișare grafic
plt.bar(df['key'], df['count'])
plt.xlabel('Cheie')
plt.ylabel('Număr apariții')
plt.title('Distribuția valorilor generate')
plt.show()