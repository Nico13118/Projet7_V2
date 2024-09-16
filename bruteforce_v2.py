import time
import csv
import os
import sys

start_time = time.time()
path = os.getcwd()
INPUT_DATA_CSV = "input_data.csv"


def get_input_data():
    csv_path = os.path.join(path, INPUT_DATA_CSV)
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        info_data = list(reader)
        return info_data


def get_data_csv(csv_file):
    """
    Fonction qui permet d'extraire les données du fichier Actions.csv.
    Function that extracts data from the Actions.csv file.
    """
    try:
        control_price_max = int(csv_file[0]['PriceMax'])
    except ValueError:
        print("Erreur constatée dans le champ PriceMax, veuillez saisir ")
        print("une valeur numérique dans le fichier input_data.csv")
        sys.exit()
    file_name = csv_file[0]['CsvFileName']
    csv_path = os.path.join(path, file_name)
    control_file = os.path.exists(csv_path)
    if control_file:
        with open(csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            list_actions = list(reader)
            return list_actions
    else:
        print(f"Nom du fichier renseigné dans input_data.csv = {file_name}")
        print("Le fichier à analyser n'existe pas dans le répertoire Projet7_V2, veuillez")
        print("contrôler votre saisie dans input_data.csv")
        sys.exit()


def filter_positive_price_and_profit(data1):
    """
    Fonction qui retourne les actions dont les valeurs de price et profit sont supérieures à 0.
    Function that returns stocks whose price and profit values are greater than 0.
    """
    new_list = [c for c in data1 if float(c['price']) > 0]
    new_list2 = [c for c in new_list if float(c['profit']) > 0]
    return new_list2


def add_value_csv(data2):
    """
    Fonction qui calcule et ajoute des valeurs dans le champ total_profit et ratio.
    Function that calculates and adds values in the total_profit and ratio fields.
    :param data2
    :return: data2
    """
    for data_csv in data2:

        value_price = float(data_csv['price'])
        pourcentage = float(data_csv['profit'])
        data_csv['result_profit'] = value_price * (pourcentage / 100)
        data_csv['ratio'] = pourcentage / value_price

    return data2


def sort_list_data(data3):
    """
    4)
    Fonction qui trie la liste.
    Function that sorts the list.
    """
    list_sort = sorted(data3, key=lambda x: float(x['profit']), reverse=True)

    return list_sort


def optimize_identical_actions(info_list=None):
    """
    Fonction qui permet de rechercher les actions qui ont le même prix et garde l'action qui a le meilleur result_profit
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


def search_best_profit(data5, data_0):
    total_price = 0
    total_result_profit = 0
    list_actions = []

    p_max = int(data_0[0]['PriceMax'])
    list_index1 = list(range(0, len(data5)))
    list_index2 = []
    for i in list_index1:
        list_index2.append(i)
        info_price = [float(data5[c]['price']) for c in list_index2]
        sum_price_actions = sum(info_price)

        info_result_profit = [float(data5[c]['result_profit']) for c in list_index2]
        sum_result_profit = sum(info_result_profit)

        if sum_price_actions <= p_max:
            if sum_result_profit > total_result_profit:
                info_action = data5[i]
                list_actions.append(info_action)
                total_price = sum_price_actions
                total_result_profit = sum_result_profit
        else:
            del list_index2[-1]
    return [data5, list_actions]


def search_to_optimize_the_result(full_list_actions=None, list_selected_actions=None):
    temp_action_list = []
    temp_total_price = 0
    temp_result_profit = 0
    """ Exclure les données list_selected_actions de full_list_actions"""
    info_list3 = [c for c in full_list_actions if c not in list_selected_actions]

    list_sorted = sorted(info_list3, key=lambda x: float(x['price']), reverse=True)
    action_list_sorted = sorted(list_selected_actions, key=lambda x: float(x['price']), reverse=True)

    for action in action_list_sorted:
        info_result_profit = float(action['result_profit'])

        result_list1 = [c for c in list_sorted if float(c['price']) < float(action['price'])]
        list_sorted2 = sorted(result_list1, key=lambda x: float(x['result_profit']), reverse=True)
        result_list2 = [c for c in list_sorted2 if float(c['result_profit']) > info_result_profit]
        if result_list2:
            action_select2 = result_list2[0]
            if action_select2 not in temp_action_list:
                temp_action_list.append(action_select2)
                temp_total_price += float(action_select2['price'])
                temp_result_profit += float(action_select2['result_profit'])
                print(result_list2[0])
            else:
                temp_action_list.append(action)
                temp_total_price += float(action['price'])
                temp_result_profit += float(action['result_profit'])
        else:
            temp_action_list.append(action)
            temp_total_price += float(action['price'])
            temp_result_profit += float(action['result_profit'])
    return [temp_action_list, temp_total_price, temp_result_profit]


def show_result(list_action=None, total_price=None, result_profit=None):
    print("Total d'achats:", total_price)
    print("Total des bénéfices:", result_profit)
    print("Liste des actions:")
    for l_action in list_action:
        print(f"{l_action['name']}: Coût: {l_action['price']} : Pourcentage: {l_action['profit']} "
              f": bénéfices: {l_action['result_profit']}")


data0 = get_input_data()
list_csv1 = get_data_csv(data0)
list_csv2 = filter_positive_price_and_profit(list_csv1)
list_csv3 = add_value_csv(list_csv2)
list_csv4 = sort_list_data(list_csv3)
list_csv5 = optimize_identical_actions(list_csv4)
final_result = search_best_profit(list_csv5, data0)
result = search_to_optimize_the_result(final_result[0], final_result[1])
show_result(result[0], result[1], result[2])


end_time = time.time()
result_time = end_time - start_time
print(f"Temps d'exécution : {result_time} seconde(s)")
