import os, sys

def part1(lines):
    state = [int(e) for e in lines[0].split(',')]
    #before running the program, replace position 1 with the value 12 and
    #replace position 2 with the value 2

    run_program(state[:])

def read_instruction(instruction):
    instruction = str(instruction)
    opcode = int(instruction[-2:])
    param_modes = [int(e) for e in reversed(list(instruction[:-2]))]

    return (opcode, param_modes)

def run_program(state):
    ip = 0

    def read_param(n, param_modes):
        mode = 0
        if len(param_modes) >= n:
            mode = param_modes[n-1]
        if mode == 0:
            # use value as pointer
            return state[state[ip + n]]
        elif mode == 1:
            # use value as-is
            return state[ip + n]
        else:
            raise Exception("unknown mode %d" % mode)

    while True:
        opcode, param_modes = read_instruction(state[ip])
        if opcode == 1: #add
            state[state[ip + 3]] = read_param(1, param_modes) + read_param(2, param_modes)
            ip += 4
        elif opcode == 2: #multiply
            state[state[ip + 3]] = read_param(1, param_modes) * read_param(2, param_modes)
            ip += 4
        elif opcode == 3: #input
            state[state[ip + 1]] = int(sys.stdin.read(1)) #needs newline, yuck
            ip += 2
        elif opcode == 4: #output
            print(str(read_param(1, param_modes)))
            ip += 2
        elif opcode == 5: #jump-if-true
            if read_param(1, param_modes) != 0:
                ip = read_param(2, param_modes)
            else:
                ip += 3
        elif opcode == 6: #jump-if-false
            if read_param(1, param_modes) == 0:
                ip = read_param(2, param_modes)
            else:
                ip += 3
        elif opcode == 7: #less than
            result = int(read_param(1, param_modes) < read_param(2, param_modes))
            state[state[ip + 3]] = result
            ip += 4
        elif opcode == 8: #equals
            result = int(read_param(1, param_modes) == read_param(2, param_modes))
            state[state[ip + 3]] = result
            ip += 4
        elif opcode == 99: #halt
            return state[0]
        else:
            raise Exception("unknown opcode %d" % opcode)



if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    part1(open(input_loc).readlines())
