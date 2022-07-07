import bext, random, sys
from time import sleep


width, height = bext.size()
width -= 1
DIR = ['dr', 'dl', 'ur', 'ul']
COLOR = ['red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white']

def main():
    bext.clear()
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    bext.fg('random')
    direction = random.choice(DIR)
    while True:
        if x == width - 3 and direction == 'dr':       # 1
            direction = 'dl'
            bext.fg(random.choice(COLOR))
        elif x == width - 3 and direction == 'ur':     # 2
            direction = 'ul'
            bext.fg(random.choice(COLOR))
        elif y == height - 1 and direction == 'dl':    # 3
            direction = 'ul'
            bext.fg(random.choice(COLOR))
        elif y == height - 1 and direction == 'dr':    # 4
            direction = 'ur'
            bext.fg(random.choice(COLOR))
        elif x == 0 and direction == 'ul':              # 5
            direction = 'ur'
            bext.fg(random.choice(COLOR))
        elif x == 0 and direction == 'dl':              # 6
            direction = 'dr'
            bext.fg(random.choice(COLOR))
        elif y == 0 and direction == 'ur':              # 7
            direction = 'dr'
            bext.fg(random.choice(COLOR))
        elif y == 0 and direction == 'ul':              # 8
            direction = 'dl'
            bext.fg(random.choice(COLOR))

        if direction == 'dr':
            x += 2
            y += 1
        if direction == 'dl':
            x -= 2
            y += 1
        if direction == 'ur':
            x += 2
            y -= 1
        if direction == 'ul':
            x -= 2
            y -= 1

        bext.goto(x, y)
        print('DVD')
        sleep(0.1)
        bext.clear()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit()
