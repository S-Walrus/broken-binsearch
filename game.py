from random import randint

n = 100
chance = 4

answer = randint(0, 100)
guess = -1
pick = False
c = 0
print('Choose your destiny!')

while not (pick and guess == answer):
    c += 1
    s = input()
    if s[0] == 'p':
        pick = True
        guess = int(s.split()[1])
        if answer == guess:
            print('Congratulations!\nIt took you ' + str(c) + ' requests')
        else:
            print('You are wrong')
    else:
        pick = False
        guess = int(s)
        lie = randint(0, chance) == 0
        if (answer > guess) ^ lie:
            print('The answer in GREATER')
        else:
            print('The answer is NOT greater')
