import re, code
from math import prod

INPUT = open('INPUT.txt', 'r').read()
INPUT = '\n'+INPUT+'\n'

PATTERN = re.compile(r"Card *(?P<card>\d+): *(?P<winning>(?:(\d+) *)*)\| *(?P<selection>(?:(\d+) *)*)")
raw = [e.groupdict() for e in PATTERN.finditer(INPUT)]
data = {int(e.pop('card')):{key: [int(g) for g in re.split(r" +", value) if g] for key, value in e.items()} for e in raw}
# What if we map all possible numbers into a series of binary, map the winning numbers, map the user numbers, then simply bitwise AND the 2 maps
# We end up with a single bit map which is simply an N-bit number, and we can easily find out how many bits in it is TRUE, then perform the score calculation
# This in theory would be the most efficient algorithm for this task.  But anyway...

score = lambda e: pow(2, e-1) if e > 0 else 0
part1 = sum([score(len([e for e in data[i]['selection'] if e in data[i]['winning']])) for i in data.keys()])

instances = dict()
for i in range(1, len(data)+1):
    instances[i] = 0

# PART 2 IS NOT GIVING CORRECT RESULT YET.
def score_instance(index, e):
    for i in range(index+1, index+e+1):
        instances[i] += 1
    return 1 + instances[index]

part2 = [score_instance(i, len([e for e in data[i]['selection'] if e in data[i]['winning']])) for i in data.keys()]

code.interact(local=locals())
