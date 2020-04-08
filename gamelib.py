from random import random, randint


class Game:
    def __init__(self, p_lie, n):
        self.answer = randint(0, n - 1)
        self.guess = -1
        self.c = 0
        self.n = n
        self.chance = p_lie

    def pick(self, guess):
        self.c += 1
        if self.answer == guess:
            return self.c
        else:
            return -1

    def req(self, guess):
        self.c += 1
        lie = random() < self.chance
        return (self.answer > guess) ^ lie
    
    def get_n(self):
        return self.answer
