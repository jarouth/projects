import random


def print_sword():
    print("                                ▓▓▓▓▓▓  ")
    print("                              ▓▓  ▒▒▓▓  ")
    print("                            ▓▓  ▒▒  ▓▓  ")
    print("                          ▓▓  ▒▒  ▓▓    ")
    print("                        ▓▓  ▒▒  ▓▓      ")
    print("                      ▓▓  ▒▒  ▓▓        ")
    print("          ▓▓▓▓      ▓▓  ▒▒  ▓▓          ")
    print("          ▓▓▒▒▓▓  ▓▓  ▒▒  ▓▓            ")
    print("            ▓▓▒▒▓▓  ▒▒  ▓▓              ")
    print("            ▓▓▒▒▓▓▒▒  ▓▓                ")
    print("              ▓▓▒▒▓▓▓▓                  ")
    print("            ▓▓▓▓▓▓▒▒▒▒▓▓                ")
    print("          ▓▓▓▓██  ▓▓▓▓▒▒▓▓              ")
    print("      ▓▓▓▓▓▓██        ▓▓▓▓              ")
    print("      ▓▓  ▓▓                            ")
    print("      ▓▓▓▓▓▓")


def print_shield():
    print("    _______________________")
    print(" / \\$$$$$$$$$$$$$$$$$$$$$$\\")
    print("(    \\$$$$$$$$$k\\;\\&j$$$$$$)")
    print("|\\     \\$$$$$$$,'    `^<$$$|")
    print("|$$\\     \\$$$;' __n,    `:$|")
    print("|$$$$\\     \\$$jT$$$$i. ,$$$|")
    print(" |$$$$$\\     \\$$$$$$$;J$$$|")
    print(" |$$$$$$$\\     \\$$$$$$$$$$|")
    print("  \\$$$$$$$$\\     \\$$$$$$$/")
    print("   \\$$$$$$$$$\\     \\$$$$/")
    print("    \\$$$$$$$$$$\\     \\$/")
    print("     \\$$$$$$$$$$$\\    /")
    print("      \\$$$$$$$$$$$$\\ /")
    print("        \\$$$$$$$$$$/")
    print("          \\$$$$$$/")
    print("            \\$$/")


def print_gun():
    print("   (                                 _")
    print("   )                               /=>")
    print("  (  +____________________/\/\___ / /|")
    print("   .''._____________'._____      / /|/\\")
    print("  : () :              :\ ----\|    \ )")
    print("   '..'______________.'0|----|      \\")
    print("                    0_0/____/        \\")
    print("                        |----    /----\\")
    print("                       || -\\\\ --|      \\")
    print("                       ||   || ||\      \\")
    print("                        \\\\____// '|      \\")
    print("Bang! Bang!                     .'/       |")
    print("                               .:/        |")
    print("                               :/_________|")


def main_game():
    user_points = 0
    computer_points = 0
    ties = 0
    options = ("Gun", "Shield", "Sword")
    quit = False

    while quit == False:
        # Get inputs
        user_input = input("Choose Gun, Shield, or sword, type exit to end game: ")
        computer_input = random.choice(options)

        # Quitting and Validation
        if user_input == "exit":
            print("Thanks for playing")
            quit = True
            continue

        if not user_input in options:
            print("Invalid Entry, try again")
            continue

        print("you selected " + user_input)
        print("the computer selected " + computer_input)

        if user_input == "Gun":
            if computer_input == "Gun":
                print("Game results in a tie")
                ties += 1
            elif computer_input == "Shield":
                print("Game results in your loss")
                computer_points += 1
            elif computer_input == "Sword":
                print("Game results in your win")
                user_points += 1

        if user_input == "Shield":
            if computer_input == "Gun":
                print("Game results in your Win")
                user_points += 1
            elif computer_input == "Shield":
                print("Game results in a tie")
                ties += 1
            elif computer_input == "Sword":
                print("Game results in your loss")
                computer_points += 1

        if user_input == "Sword":
            if computer_input == "Gun":
                print("Game results in your loss")
                computer_points += 1
            elif computer_input == "Shield":
                print("Game results in your win")
                user_points += 1
            elif computer_input == "Sword":
                print("Game results in a tie ")
                ties += 1

        art = {
            "Gun": print_gun,
            "Shield": print_shield,
            "Sword": print_sword,
        }

        art[computer_input]()
        print(
            "Your points: {}, Their points: {}, Ties: {}".format(
                user_points, computer_points, ties
            )
        )


main_game()
