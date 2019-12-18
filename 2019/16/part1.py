import os

from itertools import cycle

pattern = (0, 1, 0, -1)

def pattern(n, base_patterns=pattern):
    pattern = [[e] * (n + 1) for e in base_patterns]
    flattened = [item for sublist in pattern for item in sublist]
    iterator = cycle(flattened)
    next(iterator)
    return iterator

    #for i, d in enumerate([int(c) for c in str(n)]):
def units(n):
    return abs(n) % 10

def next_phase(digits):
    def next_digit(i, digits):
        result = 0
        for d, p in zip(digits, pattern(i)):
            result += d * p
        return units(result)
    return [next_digit(i, digits) for i in range(len(digits))]

def part1(lines, phases=100):
    digits = [int(c) for c in lines[0].strip()]

    for _ in range(phases):
        digits = next_phase(digits)
    return "".join([str(i) for i in digits[:8]])



if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    print(part1(open(input_loc).readlines()))
