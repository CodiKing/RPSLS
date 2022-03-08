from human import Human
from ai import Ai



class Game:
    def __init__(self):
        pass

    def run_game(self):
        self.display_greeting()
        self.display_rules()
        self.user_gamemode_choice()
        
        


    def display_greeting(self):
        print("Hello! Lets play a game!\n")
        print("This game is like Rock, Paper, Scissors... but more fancy!\n")
        print("Rules are, there are no rules. jk\n")

    def display_rules(self):
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

    def user_gamemode_choice(self):
        print("How would you like to play this game? With a friend or by yourself against AI?\n")
        user_input = input("Press 0 for multiplayer or 1 for Single player: ")

        if user_input == '0':
            self.player_one = Human()
            self.player_one.create_player()
            self.player_two = Human()
            self.player_two.create_player()
            self.multiplayer_game()
        elif user_input == '1':
            self.player_one = Human()
            self.player_one.create_player()
            self.player_two = Ai()
            self.player_two.create_ai()
            self.single_player()
        else:
            print('Oops! Lets pick again!')
            print("How would you like to play this game? With a friend or by yourself against AI?\n")
            user_input = input("Press 0 for multiplayer or 1 for Single player: ")
    def multiplayer_game(self):
        if self.player_one.counter >=2 or self.player_two.counter >=2:
            self.display_winner()
        else:
            self.player_one.human_choice()
            self.player_two.human_choice()
            self.comparing_gestures(self.player_one, self.player_two)

    # def human_turn(self,player_turn):
    #     self.player_turn = Human.human_choice(self)


    def single_player(self):
        if self.player_one.counter >=2 or self.player_two.counter >=2:
            self.display_winner()
        else:
            self.player_one.human_choice()
            self.player_two.random_choice()
            self.comparing_gestures_ai(self.player_one, self.player_two)


    def comparing_gestures(self,player_one, player_two):
            if player_one.player_input == 'Rock' and (player_two.player_input == 'Scissors' or player_two.player_input == 'Lizard'):
                player_one.counter += 1
                print('Player one wins!!')
                self.multiplayer_game()
            elif player_one.player_input == 'Scissors' and (player_two.player_input == 'Paper' or player_two.player_input == 'Lizard'):
                player_one.counter += 1
                print('Player one wins!!')
                self.multiplayer_game()
            elif player_one.player_input == 'Paper' and (player_two.player_input == 'Rock' or player_two.player_input == 'Spock'):
                player_one.counter += 1
                print('Player one wins!!')
                self.multiplayer_game()
            elif player_one.player_input == 'Lizard' and (player_two.player_input == 'Spock' or player_two.player_input == 'Paper'):
                player_one.counter += 1
                print('Player one wins!!')
                self.multiplayer_game()
            elif player_one.player_input == 'Spock' and (player_two.player_input == 'Scissors' or player_two.player_input == 'Rock'):
                player_one.counter += 1
                print('Player one wins!!')
                self.multiplayer_game()
            elif player_two.player_input == 'Rock' and (player_one.player_input == 'Scissors' or player_one.player_input == 'Lizard'):
                player_two.counter += 1
                print('Player two wins!!')
                self.multiplayer_game()
            elif player_two.player_input == 'Scissors' and (player_one.player_input == 'Paper' or player_one.player_input == 'Lizard'):
                player_two.counter += 1
                print('Player two wins!!')
                self.multiplayer_game()
            elif player_two.player_input == 'Paper' and (player_one.player_input == 'Rock' or player_one.player_input == 'Spock'):
                player_two.counter += 1
                print('Player two wins!!')
                self.multiplayer_game()
            elif player_two.player_input == 'Lizard' and (player_one.player_input == 'Spock' or player_one.player_input == 'Paper'):
                player_two.counter += 1
                print('Player two wins!!')
                self.multiplayer_game()
            elif player_two.player_input == 'Spock' and (player_one.player_input == 'Scissors' or player_one.player_input == 'Rock'):
                player_two.counter += 1
                print('Player two wins!!')
                self.multiplayer_game()
            if player_one.player_input == player_two.player_input:
                print('This round was a tie. Go again!')
                self.multiplayer_game()

    def comparing_gestures_ai(self,player_one,player_two):
        if player_one.player_input == 'Rock' and (player_two.player_input == 'Scissors' or player_two.player_input == 'Lizard'):
            player_one.counter += 1
            print('Player one wins!!')
            self.single_player()
        elif player_one.player_input == 'Scissors' and (player_two.player_input == 'Paper' or player_two.player_input == 'Lizard'):
            player_one.counter += 1
            print('Player one wins!!')
            self.single_player()
        elif player_one.player_input == 'Paper' and (player_two.player_input == 'Rock' or player_two.player_input == 'Spock'):
            player_one.counter += 1
            print('Player one wins!!')
            self.single_player()
        elif player_one.player_input == 'Lizard' and (player_two.player_input == 'Spock' or player_two.player_input == 'Paper'):
            player_one.counter += 1
            print('Player one wins!!')
            self.single_player()
        elif player_one.player_input == 'Spock' and (player_two.player_input == 'Scissors' or player_two.player_input == 'Rock'):
            player_one.counter += 1
            print('Player one wins!!')
            self.single_player()
        elif player_two.player_input == 'Rock' and (player_one.player_input == 'Scissors' or player_one.player_input == 'Lizard'):
            player_two.counter += 1
            print('Player two wins!!')
            self.single_player()
        elif player_two.player_input == 'Scissors' and (player_one.player_input == 'Paper' or player_one.player_input == 'Lizard'):
            player_two.counter += 1
            print('Player two wins!!')
            self.single_player()
        elif player_two.player_input == 'Paper' and (player_one.player_input == 'Rock' or player_one.player_input == 'Spock'):
            player_two.counter += 1
            print('Player two wins!!')
            self.single_player()
        elif player_two.player_input == 'Lizard' and (player_one.player_input == 'Spock' or player_one.player_input == 'Paper'):
            player_two.counter += 1
            print('Player two wins!!')
            self.single_player()
        elif player_two.player_input == 'Spock' and (player_one.player_input == 'Scissors' or player_one.player_input == 'Rock'):
            player_two.counter += 1
            print('Player two wins!!')
            self.single_player()
        if player_one.player_input == player_two.player_input:
            print('This round was a tie. Go again!')
            self.single_player()


    def display_winner(self):
        if self.player_one.counter >= 2:
            print ('Player one is the champion!')
        elif self.player_two.counter >= 2:
            print('Player two is the champion!')