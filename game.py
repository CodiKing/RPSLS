

class Game:
    def __init__(self):
        pass

    def display_greeting():
        print("Hello! Lets play a game!\n")
        print("This game is like Rock, Paper, Scissors... but more fancy!\n")
        print("Rules are, there are no rules. jk\n")


    def display_rules():
        print("""Explanation of game rules:
             Rock crushes Scissors 
             Scissors cuts Paper 
             Paper covers Rock 
             Rock crushes Lizard 
             Lizard poisons Spock 
             Spock smashes Scissors 
             Scissors decapitates Lizard 
             Lizard eats Paper
             Paper disproves Spock 
             Spock vaporizes Rock""")

    
    
    def user_gamemode_choice():
        print("How would you like to play this game? With a friend or by yourself against AI?\n")
        user_input = input("Press 0 for multiplayer or 1 for Single player: ")

        if user_input == 0:
            pass
