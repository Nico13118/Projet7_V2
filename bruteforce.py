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


def calculate_profit(combinations_lists, l_data_csv):
    """ Fonction qui permet de calculer les bénéfices de l'ensemble des combinaisons d'une liste selectionnée.
        La fonction récupère au fur et à mesure le bénéfice le plus haut, à la fin elle retourne le bénefice le plus
        haut et la combinaison associée.

    :param: combinations_lists
    :param: l_data_csv
    :return: [best_combination, [total_profit]]
    """
    total_profit = 0
    best_combination = []
    next_combi = 0
    for single_combi in combinations_lists:
        temp_profit = 0
        next_combi += 1
        for single_action_number in single_combi:
            single_action_number -= 1
            select_action = l_data_csv[single_action_number]
            select_cost_action = int(select_action['CoutParAction'])
            select_percentage_action = float(select_action['PourcentageBenefice'])
            result_profit = select_cost_action * select_percentage_action
            if next_combi == 1:
                total_profit += result_profit
            else:
                temp_profit += result_profit

        if next_combi == 1:
            best_combination = single_combi
        else:
            if temp_profit > total_profit:
                total_profit = temp_profit

                best_combination = single_combi
    return [best_combination, [total_profit]]


def show_result(f_result, l_data_csv):
    """ Fonction qui permet d'afficher la liste des actions selectionnées, le coût total et le bénéfice.

    :param: f_result
    :param: l_data_csv
    """
    total_action = 0
    print("Liste des actions selectionnées:")
    select_combination_list = f_result[0]
    select_result_profit = f_result[1]
    for single_action in select_combination_list:
        single_action -= 1
        s_action = l_data_csv[single_action]
        total_action += int(s_action['CoutParAction'])
        print(s_action)
    print("Total des actions:", total_action)
    print("Total des bénéfices:", select_result_profit[0])


list_data_csv = get_data_csv()
quantity_data_csv = len(list_data_csv) + 1
list_numbers = list(range(1, quantity_data_csv))
news_lists_combinations = generate_combinations(list_numbers)
n_combinations_lists = create_news_combinations_lists(news_lists_combinations, list_data_csv)
final_result = calculate_profit(n_combinations_lists, list_data_csv)
show_result(final_result, list_data_csv)



