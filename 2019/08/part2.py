import os, sys

def count(l, n):
    return len([e for e in l if e == n])

def part2(line, x_size=25, y_size=6):
    pixels = [int(c) for c in line]
    layer_size = x_size * y_size
    layers = [pixels[i:i+layer_size] for i in range(0, len(pixels), layer_size)]

    for y in range(y_size):
        for x in range(x_size):
            pos = y * x_size + x
            for layer in layers:
                if layer[pos] != 2:
                    break
            if layer[pos] == 0:
                sys.stdout.write("█")
            else:
                sys.stdout.write(" ")
        print()




if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    part2(open(input_loc).readlines()[0].strip())
