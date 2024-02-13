import csv
import os

path = os.getcwd()
MAX = 500


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


def create_news_combinations_lists(l_combinations, l_data_csv):
    """ Fonction qui permet de créer une nouvelle liste de combinaison.
        Elle calcule le coût de l'action dans chaque liste de combinaison.
        Si le calcul est inférieur ou égal à 500, alors la combinaison est enregistrée dans la nouvelle liste permettant
        ainsi d'écarter les combinaisons inutiles.

    :param l_combinations:
    :param l_data_csv:
    :return: news_combinations_lists
    """
    news_combinations_lists = []
    for single_combinations in l_combinations:
        actions_total_buy = 0
        for s_combinations in single_combinations:
            s_combinations -= 1
            action_select = l_data_csv[s_combinations]
            select_cost_action = action_select['CoutParAction']
            actions_total_buy += int(select_cost_action)
        if actions_total_buy <= MAX:
            news_combinations_lists.append(single_combinations)
    return news_combinations_lists


list_numbers = list(range(1, 21))
list_data_csv = get_data_csv()
news_lists_combinations = generate_combinations(list_numbers)
n_combinations_lists = create_news_combinations_lists(news_lists_combinations, list_data_csv)
print(n_combinations_lists)

