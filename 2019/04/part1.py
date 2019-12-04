import os

# $ time python3 part1.py: 2.641s

def part1(lines):
    lower, upper = lines[0].split('-')
    valid_count = 0
    #both range ends are invalid so doesn't matter if inclusive or not
    # could definitely skip loads of numbers but brute force is fast enough for before work!
    for n in range(int(lower), int(upper)):
        valid_count += valid(n)
    return valid_count


def valid(n):
    numbers = [int(d) for d in str(n)]
    if len(numbers) != 6: return False
    repeated = False
    for i in range(1, 6):
        if numbers[i-1] > numbers[i]:
            return False
        repeated = repeated or numbers[i-1] == numbers[i]
    return repeated





if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    print(part1(open(input_loc).readlines()))
