import string

input_polymer = raw_input()

def remove_units( unit_type, polymer ):
    return [c for c in polymer if not c.lower() == unit_type.lower()]

def do_stage( polymer ):
    for i, left in enumerate( polymer ):
        if i == len( polymer ) - 1:
            return None #finished!
        right = polymer[i+1]
        if left.lower() == right.lower() and left != right:
            return polymer[:i] + polymer[i+2:]

def do_reduction( full_polymer ):
    prev = full_polymer
    result = do_stage( full_polymer )
    while result is not None:
        prev = result
        result = do_stage( prev )
    return prev

for unit in string.ascii_lowercase:
    output = do_reduction( remove_units( unit, input_polymer ))
    print unit, len(output)
