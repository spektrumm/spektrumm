from pynput.mouse import Button, Controller
import time
import random

from scipy import rand

mouse = Controller()


def randNumGen(n):
    num = random.randint(0, n)
    return num


n = 600
loop = True
randNum = randNumGen(n)

while loop != False:
    time.sleep(randNum)
    mouse.move(0, 5)
    mouse.scroll(0, 2)
    mouse.move(0, -5)
    print(f'Mouse moved + scrolled after {randNum / 60} seconds')

    randNum = randNumGen(n)
