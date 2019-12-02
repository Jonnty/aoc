# did part 1 in a spreadsheet...
import math, os

def total_fuel(mass):
    total = 0
    fuel_required = fuel(mass)
    while fuel_required > 0:
        total += fuel_required
        fuel_required = fuel(fuel_required)
    return total

def fuel(mass):
    return (mass // 3) - 2

if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'real')
    masses = [int(line) for line in open(input_loc).readlines()]
    print(sum([total_fuel(mass) for mass in masses]))
