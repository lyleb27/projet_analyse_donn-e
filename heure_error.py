import pandas as pd
import matplotlib.pyplot as plt

# Chemin vers votre fichier CSV
fichier_csv = "./all_error_log.csv"

# Charger les données CSV
df = pd.read_csv(fichier_csv)

# Convertir la colonne 'timestamp' en format datetime (les dates avec microsecondes)
df['time'] = pd.to_datetime(df['time'], errors='coerce')

# Vérifiez les valeurs invalides
if df['time'].isna().sum() > 0:
    print("Certaines dates sont invalides :")
    print(df[df['time'].isna()])

# Extraire l'heure à partir des timestamps valides
df['heure'] = df['time'].dt.hour

# Compter le nombre de requêtes par heure
requetes_par_heure = df['heure'].value_counts().sort_index()

# Générer le graphique
plt.figure(figsize=(10, 6))
requetes_par_heure.plot(kind='bar', color='orange')
plt.title('Nombre de requêtes par heure')
plt.xlabel('Heure')
plt.ylabel('Nombre de requêtes')
plt.xticks(range(24), [f"{h}h" for h in range(24)], rotation=45)
plt.tight_layout()

plt.show()
