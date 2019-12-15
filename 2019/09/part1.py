import os
from collections import defaultdict
import os, sys, inspect, itertools

class ExitException(Exception):
    pass

class OutputException(Exception):
    pass

def part1(lines, inputted=[2]):
    program = [int(e) for e in lines[0].split(',')]

    return run_program(program, inputted)

def run_program(program, inputted, ip=0, relative_base=0):
    def read_instruction(instruction):
        instruction = str(instruction)
        # final two digits are opcode
        opcode = int(instruction[-2:])
        # first digits are parameter modes in reverse (without leading zeros)
        param_modes = [int(e) for e in reversed(list(instruction[:-2]))]
        return (opcode, param_modes)

    def param_mode(n, modes):
        mode = 0
        if len(modes) >= n:
            mode = modes[n-1]
        return mode

    def param(n, modes):
        # get a parameter from state according to the parameter mode
        mode = 0
        if len(modes) >= n:
            mode = modes[n-1]
        if mode == 0:
            # use value as pointer
            return state[state[ip + n]]
        elif mode == 1:
            # use value as-is
            return state[ip + n]
        elif mode == 2:
            #print("mode2 " + str(relative_base))
            return state[relative_base + state[ip + n]]
        else:
            raise Exception("unknown mode %d" % mode)

    def count_params(f):
        return len(inspect.signature(f).parameters)

    # opcode: operation, output
    def write(result, state, ip, relative_base, result_param_mode):
        if result_param_mode == 2:
            offset = relative_base
        else:
            offset = 0
        state[state[ip] + offset] = result
        # skip past the result pointer
        return ip + 1, relative_base

    def void(result, state, ip, relative_base, result_param_mode):
        # do nothing
        return ip, relative_base

    def jump(result, state, ip, relative_base, result_param_mode):
        # the result of jump functions is the ip to jump to
        return result if result is not None else ip, relative_base

    def adjust_relative_base(result, state, ip, relative_base, result_param_mode):
        #print("adj " + str(result) + " " + str(relative_base))
        return ip, relative_base + result

    def output(a):
        raise OutputException(a)

    def exit():
        raise ExitException

    state = defaultdict(int, enumerate(program))
    operations = {
        1: (lambda a, b: a + b, write),
        2: (lambda a, b: a * b, write),
        3: (lambda: inputted.pop(0), write),
        4: (output, void),
        5: (lambda a, b: b if a != 0 else None, jump),
        6: (lambda a, b: b if a == 0 else None, jump),
        7: (lambda a, b: int(a < b), write),
        8: (lambda a, b: int(a == b), write),
        9: (lambda a: a, adjust_relative_base),
        99: (exit, void)
    }

    while True:
        opcode, modes = read_instruction(state[ip])
        operation, output_handler = operations[opcode]
        param_count = count_params(operation)
        params = [param(n, modes) for n in range(1, param_count + 1)]
        ip += param_count + 1 # including opcode
        try:
            result = operation(*params)
        except OutputException as e:
            print(e.args[0])
        ip, relative_base = output_handler(result, state, ip, relative_base, param_mode(param_count + 1, modes))

if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    try:
        part1(open(input_loc).readlines())
    except ExitException:
        pass
