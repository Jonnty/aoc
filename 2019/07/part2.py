import os, sys, inspect, itertools

class ExitException(Exception):
    pass

class OutputException(Exception):
    pass

def try_settings(program, settings):
    output = 0
    states = [(program, 0)] * 5
    amp = 0
    for i in range(5):
        output, state, ip = run_program(states[amp][0], [settings[amp], output])
        states[amp] = state, ip
        amp = (amp + 1) % 5
    while True:
        try:
            output, state, ip = run_program(states[amp][0], [output], states[amp][1])
            states[amp] = state, ip
        except ExitException:
            return output
        amp = (amp + 1) % 5

def part2(lines):
    program = [int(e) for e in lines[0].split(',')]
    phase_settings = itertools.permutations([5, 6, 7, 8, 9], 5)
    return max([try_settings(program, settings) for settings in phase_settings])

# output handlers take the result, current state and ip after the params
# mutate the state if necessary and then return the new ip

def run_program(program, inputted, ip=0):

    def read_instruction(instruction):
        instruction = str(instruction)
        # final two digits are opcode
        opcode = int(instruction[-2:])
        # first digits are parameter modes in reverse (without leading zeros)
        param_modes = [int(e) for e in reversed(list(instruction[:-2]))]
        return (opcode, param_modes)

    def count_params(f):
        return len(inspect.signature(f).parameters)

    # opcode: operation, output
    def write(result, state, ip):
        state[state[ip]] = result
        # skip past the result pointer
        return ip + 1

    def void(result, state, ip):
        # do nothing
        return ip

    def jump(result, state, ip):
        # the result of jump functions is the ip to jump to
        return result if result is not None else ip

    def output(a):
        raise OutputException(a)

    def exit():
        raise ExitException

    state = program[:]
    operations = {
        1: (lambda a, b: a + b, write),
        2: (lambda a, b: a * b, write),
        3: (lambda: inputted.pop(0), write),
        4: (lambda a: output(a), void),
        5: (lambda a, b: b if a != 0 else None, jump),
        6: (lambda a, b: b if a == 0 else None, jump),
        7: (lambda a, b: int(a < b), write),
        8: (lambda a, b: int(a == b), write),
        99: (exit, void)
    }

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
        else:
            raise Exception("unknown mode %d" % mode)

    while True:
        opcode, modes = read_instruction(state[ip])
        operation, output_handler = operations[opcode]
        param_count = count_params(operation)
        params = [param(n, modes) for n in range(1, param_count + 1)]
        try:
            ip += param_count + 1 # including opcode
            result = operation(*params)
        except OutputException as e:
            return e.args[0], state, ip
        ip = output_handler(result, state, ip)



if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    print(part2(open(input_loc).readlines()))
