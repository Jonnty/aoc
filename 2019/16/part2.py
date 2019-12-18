import os

from itertools import cycle

from functools import lru_cache

pattern = (0, 1, 0, -1)

def pattern(n, base_patterns=pattern):
    pattern = [[e] * (n + 1) for e in base_patterns]
    flattened = [item for sublist in pattern for item in sublist]
    iterator = cycle(flattened)
    next(iterator)
    return iterator

def join_digits(digits):
    return "".join([str(i) for i in digits])

    #for i, d in enumerate([int(c) for c in str(n)]):
def units(n):
    return abs(n) % 10

def next_phase(digits):
    def next_digit(n, digits):
        result = 0
        n+=1
        for i in range(n-1, len(digits), 4*n):
            result += sum(digits[i:min(i+n,len(digits))])
        for i in range(3*n-1, len(digits), 4*n):
            result -= sum(digits[i:min(i+n,len(digits))])
        return units(result)
    return [next_digit(i, digits) for i in range(len(digits))]

def part2(lines, phases=100, repeat=10000, read_offset=True):
    digits = [int(c) for c in lines[0].strip()]
    digits = digits * repeat
    offset = int("".join([str(d) for d in digits[:7]])) if read_offset else 0

    for _ in range(phases):
        print(join_digits(digits[offset:offset+8]))
        digits = next_phase(digits)
    return join_digits(digits[offset:offset+8])



if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    print(part2(open(input_loc).readlines()))
