import gamelib
import sys

phi = 8
if len(sys.argv) >= 2:
    phi = int(sys.argv[1])


def start():
    game = gamelib.game()

    a = [1 for i in range(100)]
    win = False
    i = 0
    step = 100

    while True:
        if a.count(max(a)) == 1:
        #    print('Pick {}'.format(a.index(max(a))))
            x = game.pick(a.index(max(a)))
            if x != -1:
        #        print("Yeah, boyy! {} requests".format(x))
                return x
        i = -1
        c = 0
        s = sum(a)
        while c <= s//2:
            i += 1
            c += a[i]
        if i != 0 and (i == 99 or a[i-1] > a[i+1]):
            i -= 1
        #print('Ask {}'.format(i))
        if game.req(i) == 1:
            for j in range(i+1, 100):
                a[j] *= phi
        else:
            for j in range(0, i+1):
                a[j] *= phi

print(sum(start() for i in range(50)) / 50)
