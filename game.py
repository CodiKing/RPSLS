from human import Human


class Game:
    def __init__(self):
        pass

    def run_game(self):
        self.display_greeting()
        self.display_rules()
        self.user_gamemode_choice()

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
            player_one = Human()
            player_two = Human()
        elif user_input == 1:
            player_one = Human()
            player_two = Ai()
        else:
            print('Oops! Lets pick again!')
            print("How would you like to play this game? With a friend or by yourself against AI?\n")
            user_input = input("Press 0 for multiplayer or 1 for Single player: ")


    def human_turn(self):
        self.human_choice()

        pass

    def ai_turn(self):
        self.ai_choice
        pass

    def comparing_gestures(self):
        while counter < 2:
            if 
