

def search_best_profit(full_list_actions, p_max):
    """
    Cette fonction crée des listes d'actions et conserve celle qui génère le meilleur bénéfice.
    This function creates lists of actions and keeps the one that generates the highest profit.
    :param full_list_actions
    :param p_max
    :return final_action_list, total_sum_price_list, total_result_profit
    """
    p_max = int(p_max)
    total_price_list = []
    total_result_profit, number_combinations = 0.0, 0
    for n1 in full_list_actions:
        number_combinations += 1  # Incrémenter le nombre de combinaisons
        temp_total_price_list, temp_total_result_profit_list = [], []
        temp_total_price_list.append(float(n1['price']))
        temp_total_result_profit_list.append(float(n1['result_profit']))
        for n2 in full_list_actions:
            number_combinations += 1  # Incrémenter le nombre de combinaisons
            if float(n2['price']) != float(n1['price']):
                temp_total_price_list.append(float(n2['price']))
                temp_total_result_profit_list.append(float(n2['result_profit']))
                # Si la somme dépasse le prix max
                if sum(temp_total_price_list) > p_max:
                    # Retirer les dernières valeurs ajoutées pour respecter le budget
                    temp_total_price_list.pop(-1)
                    temp_total_result_profit_list.pop(-1)
        total_sum_result_profit_list = sum(temp_total_result_profit_list)
        # Si la somme de total_sum_result_profit_list et superieur
        if total_sum_result_profit_list > total_result_profit:
            # Remplacer les anciènes valeurs de total_price_list et total_result_profit
            total_price_list, total_result_profit = temp_total_price_list, total_sum_result_profit_list
    final_action_list = [c for c in full_list_actions if float(c['price']) in total_price_list]
    return [final_action_list, sum(total_price_list), total_result_profit, number_combinations]

