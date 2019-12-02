import os, sys

def part2(final):

    #before running the program, replace position 1 with the value 12 and
    #replace position 2 with the value 2
    state[1] = 12
    state[2] = 2
    return run_program(state)

def run_on(noun, verb):
    state = [int(e) for e in lines[0].split(',')]
    state[1] = noun
    state[2] = verb
    run_program(state)

def result(state, op, ptr_a, ptr_b):
    deref = lambda ptr: str(state[ptr]) if isinstance(ptr, int) else "[pos %s]" % ptr
    opcodes = {1: ' + ', 2: ' * '}
    if isinstance(op, int):
        return "(%s %s %s)" % (deref(ptr_a), opcodes[op], deref(ptr_b))
    else:
        return "(%s [op %s ] %s)" % (deref(ptr_a), op, deref(ptr_b))



def run_program_symbolic(lines):
    state = [int(e) for e in lines[0].split(',')]
    state[1] = "noun"
    state[2] = "verb"
    pos = 0
    while True:
        if state[pos] == 1 or state[pos] == 2: #add
            state[state[pos + 3]] = result(state, state[pos], state[pos + 1], state[pos + 2])
        elif state[pos] == 99: #halt
            return state[0]
        else:
            print("couldn't read opcode " + str(state[pos]))
            print(state)
            sys.exit()
        pos += 4


if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    print(run_program_symbolic(open(input_loc).readlines()))
