from random import randint


class game:

    def __init__(self):
        self.answer = randint(0, 100)
        self.guess = -1
        self.c = 0
        self.n = 100
        self.chance = 4

    def pick(self, guess):
        self.c += 1
        if self.answer == guess:
            return self.c
        else:
            return -1

    def req(self, guess):
        self.c += 1
        lie = randint(0, self.chance) == 0
        if (self.answer > guess) ^ lie:
            return 1
        else:
            return -1
    
    def get_n(self):
        return self.answer
