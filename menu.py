from bruteforce_v2 import get_input_data, check_information_entered


def show_menu():
    loop = True
    while loop:
        print("-------------Menu-------------")
        print("1) Algorithme BruteForce")
        print("2) Algorithme Optimized V1")
        print("3) Algorithme Optimized V2")
        print("4) Quitter")
        print("------------------------------")
        user_response = input("Quel est votre choix ? : ")

        x = user_response.isdigit()
        if x:
            user_response = int(user_response)
            if user_response == 1:
                print("Choix 1 ok")
            elif user_response == 2:
                print("Choix 2 ok")
            elif user_response == 3:
                print("Choix 3 ok")
            elif user_response == 4:
                print("Choix 4 ok")
            else:
                error_message()
        else:
            error_message()


def error_message():
    return print("Erreur ! Vous devez faire un choix entre la valeur 1, 2, 3 ou 4.")


show_menu()
