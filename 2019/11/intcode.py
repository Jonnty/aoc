import os
from collections import defaultdict
import os, sys, inspect, itertools

class ExitException(Exception):
    pass

class WaitForInput(Exception):
    pass

class TerminatedException(Exception):
    pass

class Intcode:

    def __init__(self, program):
        self.state = defaultdict(int, enumerate(program))
        self.inputted = []
        self.ip = 0
        self.relative_base = 0
        self.running = True

        # opcode: operation, output
        self.operations = {
            1: (lambda a, b: a + b, self.write),
            2: (lambda a, b: a * b, self.write),
            3: (self.get_input, self.write),
            4: (self.output, self.void),
            5: (lambda a, b: b if a != 0 else None, self.jump),
            6: (lambda a, b: b if a == 0 else None, self.jump),
            7: (lambda a, b: int(a < b), self.write),
            8: (lambda a, b: int(a == b), self.write),
            9: (lambda a: a, self.adjust_relative_base),
            99: (self.exit, self.void)
        }

    def run(self, *inputs):
        if not self.running:
            raise TerminatedException()
        self.outputted = []
        self.inputted = list(inputs)

        while True:
            opcode, modes = self.read_instruction(self.state[self.ip])
            operation, output_handler = self.operations[opcode]
            param_count = self.count_params(operation)
            params = [self.param(n, modes) for n in range(1, param_count + 1)]
            self.ip += param_count + 1 # including opcode
            try:
                result = operation(*params)
            except WaitForInput as e:
                self.ip -= param_count + 1 # get ready to re-run instruction
                return self.outputted
            output_handler(result, self.param_mode(param_count + 1, modes))

    def write(self, result, result_param_mode):
        if result_param_mode == 2:
            offset = self.relative_base
        else:
            offset = 0
        self.state[self.state[self.ip] + offset] = result
        # skip past the result pointer
        self.ip += 1

    def void(self, result, result_param_mode):
        pass

    def exit(self):
        raise ExitException(self.outputted)

    def jump(self, result, result_param_mode):
        # the result of jump functions is the ip to jump to
        if result is not None:
            self.ip = result

    def adjust_relative_base(self, result, result_param_mode):
        self.relative_base += result

    def output(self, a):
        self.outputted.append(a)

    def get_input(self):
        if len(self.inputted) == 0:
            raise WaitForInput()
        return self.inputted.pop(0)



    def read_instruction(self, instruction):
        instruction = str(instruction)
        # final two digits are opcode
        opcode = int(instruction[-2:])
        # first digits are parameter modes in reverse (without leading zeros)
        param_modes = [int(e) for e in reversed(list(instruction[:-2]))]
        return (opcode, param_modes)

    def param_mode(self, n, modes):
        mode = 0
        if len(modes) >= n:
            mode = modes[n-1]
        return mode

    def param(self, n, modes):
        # get a parameter from state according to the parameter mode
        mode = 0
        if len(modes) >= n:
            mode = modes[n-1]
        if mode == 0:
            # use value as pointer
            return self.state[self.state[self.ip + n]]
        elif mode == 1:
            # use value as-is
            return self.state[self.ip + n]
        elif mode == 2:
            #print("mode2 " + str(relative_base))
            return self.state[self.relative_base + self.state[self.ip + n]]
        else:
            raise Exception("unknown mode %d" % mode)

    def count_params(self, f):
        return len(inspect.signature(f).parameters)
