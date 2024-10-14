
def start_bruteforce_functions(list_csv5=None, info_price_max=None):
    final_result = search_best_profit(list_csv5, info_price_max)
    result = search_to_optimize_the_result(final_result[0], final_result[1])
    return result


def search_best_profit(full_list_actions=None, p_max=None):
    """
    Fonction qui recherche les actions qui ont le meilleur bénéfice.
    Function that searches for the stocks with the best profit.
    :param full_list_actions
    :param p_max
    :return full_list_actions, list_actions
    """
    total_price = 0
    total_result_profit = 0
    list_actions = []

    p_max = int(p_max)
    list_index1 = list(range(0, len(full_list_actions)))
    list_index2 = []
    for i in list_index1:
        list_index2.append(i)
        info_price = [float(full_list_actions[c]['price']) for c in list_index2]
        sum_price_actions = sum(info_price)

        info_result_profit = [float(full_list_actions[c]['result_profit']) for c in list_index2]
        sum_result_profit = sum(info_result_profit)

        if sum_price_actions <= p_max:
            if sum_result_profit > total_result_profit:
                info_action = full_list_actions[i]
                list_actions.append(info_action)
                total_price = sum_price_actions
                total_result_profit = sum_result_profit
        else:
            del list_index2[-1]
    return [full_list_actions, list_actions]


def search_to_optimize_the_result(full_list_actions=None, list_selected_actions=None):
    """
    Fonction qui cherche à optimiser le résultat.
    Function that seeks to optimize the result.
    :param full_list_actions:
    :param list_selected_actions:
    :return temp_action_list, temp_total_price, temp_result_profit
    """
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

