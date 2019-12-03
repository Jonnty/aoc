import os, sys, itertools

class Number:
    def __init__(self, n):
        self.value = int(n)

    def add(self, n):
        try:
            self.value += n.value
            return self
        except AttributeError:
            #it's a symbol
            return n.add(self)

    def mul(self, n):
        try:
            self.value *= n.value
            return self
        except AttributeError:
            #it's a symbol
            return n.mul(self)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)

class Symbol:
    def __init__(self, name):
        self.name = name
        self.multiplier = 1
        self.added_symbols = []
        self.added = 0

    def mul(self, n):
        self.multiplier *= n.value
        self.added *= n.value
        self.added_symbols = [s.mul(n) for s in self.added_symbols]
        return self

    def add(self, n):
        try:
            self.added += n.value
        except AttributeError:
            self.added += n.added
            n.added = 0
            self.added_symbols.append(n)
        return self


    def __str__(self):
        symbols = ""
        if self.added_symbols:
            symbols = " + " + " + ".join([str(s) for s in self.added_symbols])
        return "%d*%s + %d%s" % (self.multiplier, self.name, self.added, symbols)

    def __repr__(self):
        return str(self)

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
    deref = lambda ptr: state[ptr.value] if isinstance(ptr, Number) else Symbol("*" + str(ptr))
    opcodes = {1: '+', 2: '*'} # seems like opcodes are never overwritten :)
    opfuncs = {1: lambda a, b: a + b, 2: lambda a, b: a * b}
    a, b = deref(ptr_a), deref(ptr_b)
    if opcodes[op] == "+":
        return deref(ptr_a).add(deref(ptr_b))
    elif opcodes[op] == "*":
        return deref(ptr_a).mul(deref(ptr_b))
    else:
        raise Exception("error!")



def run_program_symbolic(state):
    pos = 0
    while True:
        if state[pos].value == 1 or state[pos].value == 2: #add
            state[state[pos + 3].value] = result(state, state[pos].value, state[pos + 1], state[pos + 2])
        elif state[pos].value == 99: #halt
            return state[0]
        else:
            print("couldn't read opcode " + str(state[pos]))
            print(state)
            sys.exit()
        pos += 4

def find_values(lines):
    instructions = [Number(n) for n in lines[0].split(',')]
    instructions[1] = Symbol("noun")
    instructions[2] = Symbol("verb")
    equation = run_program_symbolic(instructions)

    for noun in range(0, len(instructions)):
        for verb in range(0, len(instructions)):
            print(eval(str(equation), {'noun':noun, 'verb':verb}))

if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    print(find_values(open(input_loc).readlines()))
