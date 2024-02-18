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
    csv_path = os.path.join(path, "Actions.csv")
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        list_actions = list(reader)
        return list_actions


def generate_combinations(inf_data_csv):
    total_profit = 0
    total_purchase_action = 0
    best_combinations = []
    length = len(inf_data_csv)
    list_data1 = list(range(0, length))
    for ll in list(range(1, length)):  # indice de 0 à (20 exclus)
        list_data2 = combinations(list_data1, ll)
        for i in list_data2:
            select_tuple_i_left = i[:1]
            select_tuple_i_left = select_tuple_i_left[0]
            info_i = len(i)

            if info_i == 1:  # si info_i contient qu'une seule valeur
                select_action = inf_data_csv[select_tuple_i_left]
                select_purchase_action = int(select_action['CoutParAction'])
                select_profit = float(select_action['PourcentageBenefice'])
                if select_purchase_action <= MAX:
                    calculate_profit = select_purchase_action * select_profit
                    if calculate_profit > total_profit:
                        best_combinations = select_action
                        total_profit = calculate_profit
                        total_purchase_action += select_purchase_action
            else:
                temp_total_profit = 0
                temp_total_purchase_action = 0
                temp_combinations = []
                for combination in i:
                    select_action = inf_data_csv[combination]
                    select_purchase_action = int(select_action['CoutParAction'])
                    temp_total_purchase_action += select_purchase_action
                    select_profit = float(select_action['PourcentageBenefice'])
                    calculate_profit = select_purchase_action * select_profit
                    temp_total_profit += calculate_profit
                    temp_combinations.append(select_action)

                if temp_total_purchase_action < MAX:
                    if temp_total_profit > total_profit:
                        best_combinations = temp_combinations
                        total_profit = temp_total_profit
                        total_purchase_action = temp_total_purchase_action
    return [best_combinations, total_profit, total_purchase_action]


def show_result(b_result):
    select_combinations = b_result[0]
    select_profit = b_result[1]
    select_purchase_action = b_result[2]
    for combination in select_combinations:
        print(combination['NomAction'], ":", combination['CoutParAction'], ":", combination['PourcentageBenefice'])
    print("Total des achats d'actions:", select_purchase_action)
    print("Total des bénéfices:", select_profit)


info_data_csv = get_data_csv()
best_result = generate_combinations(info_data_csv)
show_result(best_result)
end_time = time.time()
result = end_time - start_time
print("Temps d'exécution du code:", result, "secondes.")