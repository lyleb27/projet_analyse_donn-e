import pandas as pd
import matplotlib.pyplot as plt

# Chemin vers votre fichier CSV
fichier_csv = "C:/Users/lebou/Documents/B3/Analyse et Exploration des données/Projet/projet_analyse_donn-e/all_error_log.csv"

# Chemin vers la base de données GeoLite2
base_geoip = "./GeoLite2-City.mmdb"

# Charger les données CSV
df = pd.read_csv(fichier_csv)

# Vérifier si la colonne 'method' existe
if 'function' not in df.columns:
    raise ValueError("La colonne 'method' est absente du fichier CSV.")

# Compter le nombre de requêtes par méthode
nombre_par_method = df['function'].value_counts()

# Afficher le résultat dans la console
print("Nombre de requêtes par méthode :")
print(nombre_par_method)

# Générer un graphique en barres
plt.figure(figsize=(10, 6))
nombre_par_method.plot(kind='bar', color='skyblue')
plt.title('Nombre de requêtes par function')
plt.xlabel('Function')
plt.ylabel('Nombre de requêtes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()