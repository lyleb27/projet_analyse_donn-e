import os
import pandas as pd

# Spécifiez le chemin du dossier contenant les fichiers CSV
dossier_csv = "C:/Users/lebou/Documents/B3/Analyse et Exploration des données/Projet/projet_analyse_donn-e/processed_e"

# Liste pour stocker les DataFrames
dataframes = []

# Parcourir tous les fichiers dans le dossier
for fichier in os.listdir(dossier_csv):
    if fichier.endswith(".csv"):
        chemin_fichier = os.path.join(dossier_csv, fichier)
        # Lire le CSV et l'ajouter à la liste
        df = pd.read_csv(chemin_fichier)
        dataframes.append(df)

# Fusionner tous les DataFrames
df_concatene = pd.concat(dataframes, ignore_index=True)

# Enregistrer le fichier fusionné
df_concatene.to_csv("C:/Users/lebou/Documents/B3/Analyse et Exploration des données/Projet/projet_analyse_donn-e/all_error_log.csv", index=False)

print("Fusion terminée !")
