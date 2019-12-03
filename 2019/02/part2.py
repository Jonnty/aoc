import os, sys

def part2(lines):
    state = [int(e) for e in lines[0].split(',')]
    #before running the program, replace position 1 with the value 12 and
    #replace position 2 with the value 2

    for noun in xrange(0, len(state)):
        for verb in xrange(0, len(state)):
            if run_program(state[:], noun, verb) == 19690720:
                return 100 * noun + verb

def run_program(state, noun, verb):
    pos = 0
    state[1] = noun
    state[2] = verb
    while True:
        if state[pos] == 1: #add
            state[state[pos + 3]] = state[state[pos + 1]] + state[state[pos + 2]]
        elif state[pos] == 2: #multiply
            state[state[pos + 3]] = state[state[pos + 1]] * state[state[pos + 2]]
        elif state[pos] == 99: #halt
            return state[0]
        else:
            print "don't know opcode " + str(state[pos])
            return None
        pos += 4


if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    print(part2(open(input_loc).readlines()))
