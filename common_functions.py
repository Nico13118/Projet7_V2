import time
import csv
import os
import bruteforce_v2
import optimized_v1_action1
import optimized_v2_action1
project_root = os.getcwd()


def start_common_functions(csv_file_name=None, info_price_max=None, algorithm_name=None):
    result = None
    start_time = time.time()

    list_csv1 = get_data_csv(csv_file_name)
    list_csv2 = filter_positive_price_and_profit(list_csv1)
    list_csv3 = add_value_csv(list_csv2)
    list_csv4 = sort_list_data(list_csv3)
    list_csv5 = optimize_identical_actions(list_csv4)

    if algorithm_name == 'bruteforce':
        result = bruteforce_v2.start_bruteforce_functions(list_csv5, info_price_max)
    elif algorithm_name == 'optimized_v1':
        result = optimized_v1_action1.start_optimized_v1_functions(list_csv5, info_price_max)
    elif algorithm_name == 'optimized_v2':
        result = optimized_v2_action1.start_optimized_v2_functions(list_csv5, info_price_max)
    show_result(result[0], result[1], result[2])

    end_time = time.time()
    result_time = end_time - start_time
    print(f"Temps d'exécution : {result_time} seconde(s)")


def get_data_csv(file_name=None):
    """
    Fonction qui permet d'extraire les données du fichier Actions.csv.
    Function that extracts data from the Actions.csv file.
    """
    csv_path = f"{project_root}/Data/{file_name}"
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        list_actions = list(reader)
        return list_actions


def filter_positive_price_and_profit(data1):
    """
    Fonction qui retourne les actions dont les valeurs de price et profit sont supérieures à 0.
    Function that returns stocks whose price and profit values are greater than 0.
    """
    new_list = [c for c in data1 if float(c['price']) > 0]
    new_list2 = [c for c in new_list if float(c['profit']) > 0]
    print()
    return new_list2


def add_value_csv(data2):
    """
    Fonction qui calcule et ajoute des valeurs dans le champ result_profit et ratio.
    Function that calculates and adds values in the total_profit and ratio fields.
    :param data2
    :return data2
    """
    for data_csv in data2:

        value_price = float(data_csv['price'])
        pourcentage = float(data_csv['profit'])
        data_csv['result_profit'] = value_price * (pourcentage / 100)
        data_csv['ratio'] = pourcentage / value_price

    return data2


def sort_list_data(data3):
    """
    Fonction qui trie le champ profit du plus grand au plus petit.
    Function that sorts the profit field from largest to smallest.
    :param : data3
    :return : list_sort
    """
    list_sort = sorted(data3, key=lambda x: float(x['profit']), reverse=True)

    return list_sort


def optimize_identical_actions(info_list=None):
    """
    Fonction qui permet de rechercher les actions qui ont le même prix et garde l'action qui a le meilleur
    result_profit.
    Function that allows you to search for stocks that have the same price and keep the stock that has the best
    result_profit.
    :param info_list
    :return new_list
    """
    new_list = []
    for action in info_list:
        price_action = float(action['price'])
        control_action = [c for c in new_list if float(c['price']) == price_action]
        if not control_action:
            action_temp = [c for c in info_list if float(c['price']) == price_action]
            if len(action_temp) == 1:
                new_list.append(action_temp[0])
            else:
                action_temp_sort = sorted(action_temp, key=lambda x: x['ratio'], reverse=True)
                new_list.append(action_temp_sort[0])

    return new_list


def show_result(list_action=None, total_price=None, result_profit=None):
    """
    Fonction qui affiche le résultat.
    Function that displays the result.
    :param list_action
    :param total_price
    :param result_profit
    """
    print("Liste des actions:")
    for l_action in list_action:
        print(f"{l_action['name']}: Coût: {l_action['price']} : Pourcentage: {l_action['profit']} "
              f": bénéfices: {l_action['result_profit']}")
    print("Total d'achats:", total_price)
    print("Total des bénéfices:", result_profit)
