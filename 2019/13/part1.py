import os
import intcode

def part1(lines):
    program = [int(e) for e in lines[0].split(',')]
    code = intcode.Intcode(program)
    output = code.run()
    print(output)
    return len([e for i, e in enumerate(output) if i % 3 == 2 and e == 2])

if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    print(part1(open(input_loc).readlines()))
