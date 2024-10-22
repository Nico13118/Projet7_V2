from itertools import combinations


def generate_combination(data_csv, p_max):
    p_max, n_data = int(p_max), len(data_csv)
    final_list = []
    total_price, total_result_profit, number_combinations = 0, 0, 0
    for i in list(range(1, n_data)):
        result_comb = combinations(data_csv, i)
        for r_comb in result_comb:
            number_combinations += 1
            if len(r_comb) == 1:
                r_comb = r_comb[0]
                action_price = float(r_comb['price'])
                if action_price <= p_max:
                    action_result_profit = float(r_comb['result_profit'])
                    if action_result_profit > total_result_profit:
                        final_list, total_price, total_result_profit = [r_comb], action_price, action_result_profit
            else:
                action_price = [float(c['price']) for c in r_comb]
                if sum(action_price) <= p_max:
                    action_result_profit = [c['result_profit'] for c in r_comb]
                    if sum(action_result_profit) > total_result_profit:
                        final_list = [c for c in r_comb]
                        total_price, total_result_profit = sum(action_price), sum(action_result_profit)
    return [final_list, total_price, total_result_profit, number_combinations]
