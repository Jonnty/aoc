import os, sys

def part1(lines):
    state = [int(e) for e in lines[0].split(',')]
    #before running the program, replace position 1 with the value 12 and
    #replace position 2 with the value 2
    state[1] = 12
    state[2] = 2
    return run_program(state)

def run_program(state):
    pos = 0
    while True:
        if state[pos] == 1: #add
            state[state[pos + 3]] = state[state[pos + 1]] + state[state[pos + 2]]
        elif state[pos] == 2: #multiply
            state[state[pos + 3]] = state[state[pos + 1]] * state[state[pos + 2]]
        elif state[pos] == 99: #halt
            return state[0]
        else:
            print("error!")
            sys.exit()
        pos += 4


if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    print(part1(open(input_loc).readlines()))
