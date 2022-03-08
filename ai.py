import random

from person import Person 

class Ai(Person):
    def __init__(self):
        super().__init__()


    def create_ai(self):
        self.counter = 0

    def random_choice(self):
        self.player_input = random.choice(self.gesture_list)
