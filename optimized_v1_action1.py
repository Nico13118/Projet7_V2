import csv
import os
import time

path = os.getcwd()
start_time = time.time()
PRICE_MAX = 500


def get_data_csv():
    """
    Fonction qui permet d'extraire les données du fichier Actions1.csv
    """
    csv_path = os.path.join(path, "Actions1.csv")
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        list_actions = list(reader)
        return list_actions


def modify_list_csv(data1):
    """
    2)
    Fonction qui garde les valeurs de price superieur à 1.
    """
    new_list = [c for c in data1 if float(c['price']) > 1]
    return new_list


def add_value_csv(data2):
    """
    3)
    Fonction qui calcul et ajoute des valeurs dans le champ total_benefice
    """
    for data_csv in data2:

        value_price = float(data_csv['price'])
        pourcentage = float(data_csv['profit'])
        data_csv['total_benefice'] = value_price * (pourcentage / 100)

    return data2


list_csv1 = get_data_csv()
list_csv2 = modify_list_csv(list_csv1)
list_csv3 = add_value_csv(list_csv2)
