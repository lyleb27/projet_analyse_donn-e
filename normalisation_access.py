import re
import pandas as pd
from datetime import datetime

# Fonction pour parser les lignes de Access.log
def parse_access_log_line(line):
    # Regex pour extraire les champs
    log_pattern = r'(?P<ip>\S+) \S+ \S+ \[(?P<timestamp>.*?)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d+) (?P<size>\S+) "(?P<referer>.*?)" "(?P<user_agent>.*?)"'
    match = re.match(log_pattern, line)
    if match:
        return match.groupdict()
    return None

# Fonction pour convertir le timestamp en Unix timestamp
def convert_to_unix_timestamp(timestamp):
    # Format du timestamp dans le fichier log
    log_time_format = "%d/%b/%Y:%H:%M:%S %z"
    dt = datetime.strptime(timestamp, log_time_format)
    return int(dt.timestamp())

# Lecture du fichier Access.log
def process_access_log(file_path):
    records = []
    with open(file_path, 'r') as file:
        for line in file:
            log_entry = parse_access_log_line(line)
            if log_entry:
                # Convertir le timestamp
                log_entry['timestamp'] = convert_to_unix_timestamp(log_entry['timestamp'])
                # Convertir la taille en entier ou remplacer par 0 si "-"
                log_entry['size'] = int(log_entry['size']) if log_entry['size'].isdigit() else 0
                records.append(log_entry)
    # Création d'un DataFrame
    df = pd.DataFrame(records)
    return df

# Chemin vers le fichier Access.log
access_log_path = "C:/Users/lebou/Documents/B3/Analyse et Exploration des données/Projet/projet_analyse_donn-e/Access.log/access.log-20240616" # --> à remplir

# Traitement du fichier
df_access = process_access_log(access_log_path)

# Aperçu des données
print(df_access.head())

# Sauvegarde en CSV si besoin
df_access.to_csv("C:/Users/lebou/Documents/B3/Analyse et Exploration des données/Projet/projet_analyse_donn-e/processed_access_log_9.csv", index=False)

