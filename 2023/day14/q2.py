from functools import cache
def print_map(one):
    for i in one:
        print("".join(c for c in i))
    print('')

with open('puzzle', 'r') as f:
    puzzle = f.read()
one = puzzle.strip()


@cache
def slip(one):
    while one.find('.O') != -1: one = one.replace('.O','O.')
    return one

@cache
def left(text):
    lines = text.split('\n')
    # Zip the lines together after reversing the order of characters in each line
    return '\n'.join(''.join(t) for t in zip(*[line[::-1] for line in lines]))

@cache
def right(text):
    lines = text.split('\n')
    # Zip the lines together and then reverse the order of characters in each resulting line
    return '\n'.join(''.join(t)[::-1] for t in zip(*lines))

@cache
def one_cycle(one):
    one = right(slip(left(one)))
    one = slip(one)
    one = left(slip(right(one)))
    one = left(left(slip(right(right(one)))))
    return one

def get_score(one):
    one = one.split('\n')
    total = len(one)
    score = 0
    i = 0 
    while i < total:
        num_o = sum(1 for c in one[i] if c == 'O')
        score += (num_o*(total - i))
        i+= 1
    
    return score


def loop(part):
    for _ in range(1000000000):
        part = one_cycle(part)
    return part

    
print(get_score(loop(one)))
