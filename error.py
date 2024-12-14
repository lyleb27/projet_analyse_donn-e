import re
import json
import pandas as pd
import matplotlib.pyplot as plt

# Fonction de prétraitement pour nettoyer les lignes du fichier log
def preprocess_line(line):
    line = re.sub(r'\\"', "'", line)
    return line

# Fonction pour sauvegarder les données dans un fichier CSV
def save_to_csv(df, output_file):
    df.to_csv(output_file, index=False)
    print(f"Les données ont été sauvegardées dans {output_file}")

# Fonction pour parser une ligne du fichier log
def parse_log_line(line):
    try:
        # Pré-traiter la ligne avant de la parser
        processed_line = preprocess_line(line)
        log_data = json.loads(processed_line)  # Conversion en JSON
        return log_data
    except json.JSONDecodeError:
        # Si le format JSON est incorrect, on ignore cette ligne
        print(f"Ligne ignorée : {line} - Erreur JSONDecodeError")
        return None

# Fonction pour traiter le fichier de logs et le convertir en DataFrame
def process_log_file(file_path):
    log_entries = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            log_data = parse_log_line(line)
            if log_data:
                log_entries.append(log_data)
    
    # Création d'un DataFrame à partir des données traitées
    df = pd.DataFrame(log_entries)
    return df


# Fonction principale
def main():
    # Spécifiez le chemin du fichier de logs
    file_path = "error.log-20240519" # --> à changer (non automatisé)
    output_file = "processed_error_log_9.csv" # --> à changer (non automatisé)

    # Traitement du fichier et création du DataFrame
    df = process_log_file(file_path)

    # Si des données valides ont été extraites, afficher le graphique
    if not df.empty:
        save_to_csv(df, output_file)
    else:
        print("Le DataFrame est vide. Aucun log valide traité.")

if __name__ == "__main__":
    main()


# "C:/Users/lebou/Documents/B3/Analyse et Exploration des données/Projet/Error.log/error.log-20240428"