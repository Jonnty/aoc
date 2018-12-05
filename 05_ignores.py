import string

input_polymer = raw_input()

def initial_ignores( unit_type, polymer ):
    return [i for i, c in enumerate(polymer) if c.lower() == unit_type.lower()]

def do_stage( polymer, ignore ):
    for leftIndex, left in enumerate( polymer ):
        if leftIndex in ignore:
            continue
        rightIndex = leftIndex + 1
        while rightIndex in ignore:
            rightIndex += 1

        if rightIndex >= len( polymer ):
                return None

        right = polymer[rightIndex]
        if left.lower() == right.lower() and left != right:
            return leftIndex, rightIndex
    return None

def do_reduction( full_polymer, initial_ignore ):
    ignore = set(initial_ignore)
    result = do_stage( full_polymer, ignore )
    while result is not None:
        ignore.add(result[0])
        ignore.add(result[1])
        result = do_stage( full_polymer, ignore )
    return [c for i, c in enumerate(full_polymer) if not i in ignore]

for unit in string.ascii_lowercase:
    output = do_reduction( input_polymer, initial_ignores( unit, input_polymer ))
    print unit, len(output)
