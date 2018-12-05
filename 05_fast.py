import string

def collision(a, b):
    return a.lower() == b.lower() and a != b

def reduce(polymer, ignored=None):
    if ignored:
        ignored = ignored.lower()
    raw = polymer[:] #make a copy so that we don't lose the original polymer for later use
    out = []
    while len(raw) > 0:
        next = raw.pop(0)
        if ignored == next.lower():
            continue
        if out and collision(out[-1], next):
            out.pop()
        else:
            out.append(next)

    return "".join(out)

polymer = list(raw_input())

print "part 1"
out = reduce(polymer)
print out
print len(out)
print
print "part 2"
for unit in string.ascii_lowercase:
    out = reduce(polymer, unit)
    print unit, len(out)
