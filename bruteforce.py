import csv
import os

path = os.getcwd()


def get_data_csv():
    """ Fonction qui permet d'extraire les données du fichier Action.csv

    :return: list_actions
    """
    csv_path = os.path.join(path, "Actions.csv")
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        list_actions = list(reader)
        return list_actions


list_data_csv = get_data_csv()

