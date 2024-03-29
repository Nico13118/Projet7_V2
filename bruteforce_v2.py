from itertools import combinations
import time
import csv
import os

start_time = time.time()
path = os.getcwd()
MAX = 500


def get_data_csv():
    """ Fonction qui permet d'extraire les données du fichier Action.csv

    : return : list_actions
    """
    csv_path = os.path.join(path, "Actions2.csv")
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


list_csv1 = get_data_csv()
list_csv2 = modify_list_csv(list_csv1)