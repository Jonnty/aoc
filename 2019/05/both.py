import os, sys, inspect

class ExitException(Exception):
    pass

def both(lines):
    state = [int(e) for e in lines[0].split(',')]
    run_program(state[:])

def read_instruction(instruction):
    instruction = str(instruction)
    # final two digits are opcode
    opcode = int(instruction[-2:])
    # first digits are parameter modes in reverse (without leading zeros)
    param_modes = [int(e) for e in reversed(list(instruction[:-2]))]
    return (opcode, param_modes)

def count_params(f):
    return len(inspect.signature(f).parameters)

# output handlers take the result, current state and ip after the params
# mutate the state if necessary and then return the new ip

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

def exit():
    raise ExitException

# opcode: operation, output
operations = {
    1: (lambda a, b: a + b, write),
    2: (lambda a, b: a * b, write),
    3: (lambda: int(sys.stdin.read(1)), write),
    4: (lambda a: print(str(a)), void),
    5: (lambda a, b: b if a != 0 else None, jump),
    6: (lambda a, b: b if a == 0 else None, jump),
    7: (lambda a, b: int(a < b), write),
    8: (lambda a, b: int(a == b), write),
    99: (exit, void)
}

def run_program(state):
    ip = 0
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
            result = operation(*params)
        except ExitException:
            return
        ip += param_count + 1 # including opcode
        ip = output_handler(result, state, ip)



if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    both(open(input_loc).readlines())
