import pandas as pd
import matplotlib.pyplot as plt
from geoip2.database import Reader

# Chemin vers votre fichier CSV
fichier_csv = "C:/Users/lebou/Documents/B3/Analyse et Exploration des données/Projet/projet_analyse_donn-e/all_access_log.csv"

# Chemin vers la base de données GeoLite2
base_geoip = "./GeoLite2-City.mmdb"

# Charger les données CSV
df = pd.read_csv(fichier_csv)

# Créer une colonne 'pays' à partir des adresses IP
def obtenir_pays(ip, reader):
    try:
        # Utilisation de GeoIP2 pour récupérer le pays
        response = reader.city(ip)
        return response.country.name
    except:
        return "Inconnu"

# Charger la base de données GeoLite2
reader = Reader(base_geoip)

# Appliquer la fonction pour obtenir les pays
df['pays'] = df['ip'].apply(lambda ip: obtenir_pays(ip, reader))

# Compter le nombre d'occurrences par pays
compte_pays = df['pays'].value_counts()

# Filtrer les pays avec au moins 75 requêtes
compte_pays_filtre = compte_pays[compte_pays >= 75]

# Fermer le lecteur GeoIP2
reader.close()

# Afficher le graphique
plt.figure(figsize=(12, 6))
compte_pays_filtre.plot(kind='bar', color='skyblue')
plt.title('Nombre de requêtes par pays (au moins 75 requêtes)')
plt.xlabel('Pays')
plt.ylabel('Nombre de requêtes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
