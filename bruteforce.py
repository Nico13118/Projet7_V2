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


def generate_combinations(l_numbers):
    """ Fonction qui permet de créer toutes les combinaisons possibles de 1 à 20.
        Créer plusieurs listes contenant au minimum 4 combinaison
    :param l_numbers:
    :return: list_combinations
    """
    n = len(l_numbers)
    list_combinations = []
    for i in range(1 << n):
        temp_combination_list = []
        for j in range(n):
            if (i >> j) & 1:
                temp_combination_list.append(l_numbers[j])
        if temp_combination_list:
            if len(temp_combination_list) >= 4:
                list_combinations.append(temp_combination_list)
    return list_combinations


list_numbers = list(range(1, 21))
list_data_csv = get_data_csv()
list_combination = generate_combinations(list_numbers)


