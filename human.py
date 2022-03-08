from person import Person


class Human(Person):
    def __init__(self):
        super().__init__()

  

    def human_choice(self):
        print("What would you like to throw??\n")
        print(f"""Press: 0 for Rock
        Press: 1 for Scissors
        Press: 2 for Paper
        Press: 3 for Lizard
        Press: 4 for Spock""")

        
        self.player_input =  int(input("Please select a number: "))
        if self.player_input == 0:
             self.player_input = 'Rock'
        elif self.player_input == 1:
            self.player_input = 'Scissors'
        elif self.player_input == 2:
            self.player_input = 'Paper'
        elif self.player_input == 3:
            self.player_input = 'Lizard'
        elif self.player_input == 4:
            self.player_input = 'Spock'
        else:
            print('Try again.')
            self.player_input =  int(input("Please select a number: "))
        
    def create_player(self):
        self.counter = 0
        
    