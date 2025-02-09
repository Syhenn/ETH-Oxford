import json
import os

def load_data(file_path):
    """Charge les données depuis un fichier JSON."""
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

def save_data(file_path, data):
    """Sauvegarde les données dans un fichier JSON."""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def add_or_update_crypto(file_path, crypto_name, score):
    """Ajoute ou met à jour une cryptomonnaie dans le JSON."""
    data = load_data(file_path)
    clean_string = crypto_name.strip("'")
    if crypto_name not in data:
        data[crypto_name] = 0
    data[clean_string] += score 
    save_data(file_path, data)
    print(f"{crypto_name} mis à jour avec un score de {score}.")
def excecute(datas):
    for data in datas:
        add_or_update_crypto(file_path, data['Crypto'], data['Score'])

file_path = "cryptos.json"