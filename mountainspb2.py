mountains_file = r"CodeSinaia-2025\IntroToPy\mountains_db.tsv"

mountd = {"nume": [], "metri": [], "tara": [], "cod": []}

with open(mountains_file, "r", encoding="utf-8") as f:
    for line in f:
        #print(line)
        parts = line.strip().split('\t')
        if len(parts) != 4:
            continue
        nume, metri, tara, cod = parts
        mountd["nume"].append(nume)
        mountd["metri"].append(metri)
        mountd["tara"].append(tara)
        mountd["cod"].append(cod)

# Convertim valorile 'metri' la int, ignorând valorile lipsă sau invalide
metri_valide = []
nume_valide = []
for nume, metri in zip(mountd["nume"], mountd["metri"]):
    
    
    #print(metri)
    if metri != 'NULL':
        m = float(metri)
        if(m!=0):
            metri_valide.append(m)
            nume_valide.append(nume)

if metri_valide:
    min_idx = metri_valide.index(min(metri_valide))
    max_idx = metri_valide.index(max(metri_valide))
    print(f"Cel mai mic munte: {nume_valide[min_idx]} ({metri_valide[min_idx]} m)")
    print(f"Cel mai înalt munte: {nume_valide[max_idx]} ({metri_valide[max_idx]} m)")
else:
    print("Nu există valori valide pentru înălțime.")


import matplotlib.pyplot as plt
import numpy as np

# ...existing code...

# Construim country_mountains folosind doar valorile din metri_valide
country_mountains = {}
for nume, metri, cod in zip(nume_valide, metri_valide, mountd["cod"]):
    if cod not in country_mountains:
        country_mountains[cod] = []
    country_mountains[cod].append(metri)

# 5. Bar: cod țară vs număr munți
codes = list(country_mountains.keys())
counts = [len(country_mountains[c]) for c in codes]
plt.figure(figsize=(10, 4))
plt.bar(codes, counts)
plt.xlabel("Cod țară (ISO)")
plt.ylabel("Număr munți")
plt.title("Numărul de munți înregistrați pe țară")
plt.tight_layout()
plt.show()

# 6. Bar: cod țară vs altitudine maximă
max_heights = [max(country_mountains[c]) for c in codes]
plt.figure(figsize=(10, 4))
plt.bar(codes, max_heights)
plt.xlabel("Cod țară (ISO)")
plt.ylabel("Altitudine maximă (m)")
plt.title("Altitudinea maximă a munților pe țară")
plt.tight_layout()
plt.show()

# 7. Boxplot: distribuția altitudinii globale
all_heights = []
for heights in country_mountains.values():
    all_heights.extend(heights)
plt.figure(figsize=(6, 4))
plt.boxplot(all_heights, vert=True, patch_artist=True)
plt.ylabel("Altitudine (m)")
plt.title("Distribuția altitudinii munților (toate țările)")
plt.tight_layout()
plt.show()

# 8. Bar compus: cod țară vs min/median/max altitudine
mins = [min(country_mountains[c]) for c in codes]
medians = [np.median(country_mountains[c]) for c in codes]
maxs = [max(country_mountains[c]) for c in codes]

x = np.arange(len(codes))
width = 0.25

plt.figure(figsize=(12, 5))
plt.bar(x - width, mins, width, label='Minim')
plt.bar(x, medians, width, label='Mediană')
plt.bar(x + width, maxs, width, label='Maxim')
plt.xlabel("Cod țară (ISO)")
plt.ylabel("Altitudine (m)")
plt.title("Altitudinea minimă, mediană și maximă pe țară")
plt.xticks(x, codes, rotation=45)
plt.legend()
plt.tight_layout()
plt.show()