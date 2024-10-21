
def start_bruteforce_functions(list_csv5, info_price_max):
    final_result = search_best_profit(list_csv5, info_price_max)
    return final_result


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
    total_result_profit = 0
    for n1 in full_list_actions:
        """
        Cette boucle récupère la première actions.
        Récupération de la valeur 'price' qu'on ajoute dans 'temp_total_price_list'
        Récupération de la valeur 'result_profit' qu'on ajoute dans 'temp_total_result_profit_list'
         
        """
        price_n1, result_profit_n1 = float(n1['price']), float(n1['result_profit'])
        temp_total_price_list, temp_total_result_profit_list = [], []
        temp_total_price_list.append(price_n1)
        temp_total_result_profit_list.append(result_profit_n1)
        for n2 in full_list_actions:
            price_n2, result_profit_n2 = float(n2['price']), float(n2['result_profit'])
            if price_n2 != price_n1:
                """
                Ajout de price_n2 dans temp_total_price_list
                Ajout de result_profit_n2 dans temp_total_result_profit_list
                """
                temp_total_price_list.append(price_n2)
                temp_total_result_profit_list.append(result_profit_n2)
                """
                Calculer la somme temp_total_price_list.
                """
                total_sum_price_list = sum(temp_total_price_list)
                if total_sum_price_list > p_max:
                    """ 
                    Si le total est superieur au prix max, on retire les dernières valeurs ajouté dans les deux listes   
                    """
                    temp_total_price_list.pop(-1)
                    temp_total_result_profit_list.pop(-1)
        """
        Calculer la somme de temp_total_result_profit_list
        """
        total_sum_result_profit_list = sum(temp_total_result_profit_list)
        if total_sum_result_profit_list > total_result_profit:
            """
            Si total_sum_result_profit_list est superieur à total_result_profit, on ajoute :
            temp_total_price_list dans total_price_list.
            total_sum_result_profit_list dans total_result_profit
            """
            total_price_list, total_result_profit = temp_total_price_list, total_sum_result_profit_list
    final_action_list = [c for c in full_list_actions if float(c['price']) in total_price_list]
    total_sum_price_list = sum(total_price_list)
    return [final_action_list, total_sum_price_list, total_result_profit]

