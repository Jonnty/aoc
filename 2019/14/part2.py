import os

from math import ceil
from collections import defaultdict

class Chemical:

    def __init__(self, n, chemical):
        self.n = n
        self.chemical = chemical

    def mul(self, m):
        self.n * m

    def __repr__(self):
        return "%d%s" % (self.n, self.chemical)

def line2reaction(line):
    inp, out = [l.strip() for l in line.split("=>")]
    inp = [c.strip() for c in inp.split(",")]
    inp = [c.split() for c in inp]
    out = out.split()
    inp = [Chemical(int(c[0]), c[1]) for c in inp]
    out = Chemical(int(out[0]), out[1])
    return out.chemical, (inp, out)



def part2(lines):
    raw_reactions = [line2reaction(line) for line in lines]
    reactions = dict(raw_reactions)
    assert len(raw_reactions) == len(reactions)
    requirements = defaultdict(int, [("FUEL", 1863741)]) # manually searched :P
    spare = defaultdict(int) # need to handle this too
    ore = 0
    while len(requirements) > 0:
        required_chemical = list(requirements.keys())[0]
        required_n = requirements[required_chemical]
        del requirements[required_chemical]
        if required_chemical == "ORE":
            ore += required_n
            continue
        output_n = reactions[required_chemical][1].n
        multiple = ceil(required_n / output_n)
        produced = output_n * multiple
        spare[required_chemical] = produced - required_n
        for new_req in reactions[required_chemical][0]:
            requirements[new_req.chemical] += (new_req.n * multiple) - spare[new_req.chemical]
            del spare[new_req.chemical]
            if requirements[new_req.chemical] < 0:
                spare[new_req.chemical] = -requirements[new_req.chemical]
                del requirements[new_req.chemical]



    return ore / 1000000000000





if __name__ == "__main__":
    input_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    print(part2(open(input_loc).readlines()))
