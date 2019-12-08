import os

def count(l, n):
    return len([e for e in l if e == n])

def part1(line, dimensions=(25, 6)):
    pixels = [int(c) for c in line]
    layer_size = dimensions[0] * dimensions[1]
    layers = [pixels[i:i+layer_size] for i in range(0, len(pixels), layer_size)]

    result = min(layers, key=lambda l: count(l, 0))
    return count(result, 1) * count(result, 2)


if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    print(part1(open(input_loc).readlines()[0].strip()))
