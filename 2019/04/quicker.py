import os

# $ time python3 quicker.py
# 222222
# part 1: 1873
# part 2: 1264
#
# real	0m0.077s

def both(lines):
    lower, upper = lines[0].split('-')
    valid_count1, valid_count2 = 0, 0

    for n in gen_numbers(int(lower), int(upper)):
        valid_count1 += valid1(n)
        valid_count2 += valid2(n)

    print("part 1: %d" % valid_count1)
    print("part 2: %d" % valid_count2)


def get_digits(n):
    result = []
    while n:
        result.insert(0, n % 10)
        n //= 10
    return result

def gen_numbers(mini, maxi):
    length = 6 # what's the harm?
    n = mini
    while n <= maxi:
        old_n = n
        digits = get_digits(n)
        for i in range(1, length):
            prev, curr = digits[i-1], digits[i]
            if prev > curr:
                n += (prev - curr) * (10 ** (length - i - 1))
                break

        if n == old_n:
            yield n
            n += 1

        #136788


def valid1(n):
    if 222000 < n < 222223:
        print(n)
    numbers = [int(d) for d in str(n)]
    if len(numbers) != 6: return False
    repeated = False
    for i in range(1, 6):
        if numbers[i-1] > numbers[i]:
            return False
        repeated = repeated or numbers[i-1] == numbers[i]
    return repeated

def valid2(n):
    numbers = [int(d) for d in str(n)]
    if len(numbers) != 6: return False
    repeated = False # now means EXACTLY twice
    groupsize = 0
    for i in range(1, 6):
        if numbers[i-1] > numbers[i]:
            return False
        if numbers[i-1] != numbers[i]:
            if groupsize == 2: repeated = True
            groupsize = 0
        else:
            if groupsize == 0 : groupsize = 2
            else: groupsize += 1
    return repeated or groupsize == 2

if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    both(open(input_loc).readlines())
