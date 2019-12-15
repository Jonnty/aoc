import os, sys
import intcode
import subprocess as sp

# 0 is an empty tile. No game object appears in this tile.
# 1 is a wall tile. Walls are indestructible barriers.
# 2 is a block tile. Blocks can be broken by the ball.
# 3 is a horizontal paddle tile. The paddle is indestructible.
# 4 is a ball tile. The ball moves diagonally and bounces off objects.
tiles = [" ", "*", "#", "-", "O"]
def draw(output):
    score = output[(-1, 0)]
    maxX = max([x for x, y in output.keys()])
    maxY = max([y for x, y in output.keys()])

    for y in range(maxY):
        for x in range(maxX):
            sys.stdout.write(tiles[output[(x,y)]])
        print()
    print(score)

def part2(lines):
    program = [int(e) for e in lines[0].split(',')]
    program[0] = 2 # play for free
    code = intcode.Intcode(program)
    screen = {}
    while True:
        print(">")
        # inp = sys.stdin.read(1)
        # if not inp in ["1", "2", "3"]: continue
        output = code.run(0)
        groups = [ output[i:i+3] for i in range(0, len(output), 3) ]
        output = [((x,y), e) for x, y, e in groups]
        screen.update(output)
        sp.call('clear',shell=True)
        draw(screen)

if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    part2(open(input_loc).readlines())
