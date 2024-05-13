import re, code
from math import prod

INPUT = open('INPUT.txt', 'r').read()
INPUT = '\n'+INPUT+'\n'

raw = [e for e in re.split(r"\n+", INPUT) if e]

NUM = re.compile(r"\d+", re.I)
SYM = re.compile(r"[^.\d\s]+", re.I)

POS_NUM = tuple()
# PART 1 Result

adjacent = lambda tup: tuple([tup[0]-1, tup[1]])
# Match.span gives index of the 1st char and then the index+1 of the last char
validify = lambda index, tup: tup[0] <= index <= tup[1]
# Check the index of a symbol within 2 adjacent lines to fall within Match.span of the number, then it is a valid part number

for i, line in enumerate(raw):
    POS_SYM = [e.start() for e in SYM.finditer(raw[i-1])] if i > 0 else []
    POS_SYM.extend([e.start() for e in SYM.finditer(line)]) # Initially I neglected the symbols on the same line - which is technically adjacent! mind you!
    POS_SYM.extend([e.start() for e in SYM.finditer(raw[i+1])] if i < len(raw)-1 else [])
    # Gets the index number of all symbols from all adjacent lines
    POS_NUM += tuple(int(e.group()) for e in NUM.finditer(line) if any([validify(i, adjacent(e.span())) for i in POS_SYM]))
    # Store number if its adjacent span touches any symbol.

    # RANT: MY ANSWER WAS CORRECT AT THIS POINT BUT SOMEHOW AOC TELLS ME IT WAS WRONG AND I FRUSTRATED OVER THIS DAMN THING FOR 30 MORE MINUTES FINDING ABSOLUTELY NO OTHER LOGICAL ISSUES
    # GOD DAMN IT...

GEAR = re.compile(r"\*", re.I)

POS_GEAR = tuple()
# PART 2 Result

for i, line in enumerate(raw):
    GEAR_POS = [e.start() for e in GEAR.finditer(line)]
    if GEAR_POS:
        for pos in GEAR_POS:
            NUMBERS = [int(e.group()) for e in NUM.finditer(raw[i-1]) if validify(pos, adjacent(e.span()))] if i > 0 else []
            NUMBERS.extend([int(e.group()) for e in NUM.finditer(line) if validify(pos, adjacent(e.span()))])
            NUMBERS.extend([int(e.group()) for e in NUM.finditer(raw[i+1]) if validify(pos, adjacent(e.span()))] if i < len(raw)-1 else [])
            if len(NUMBERS) == 2:
                POS_GEAR += (NUMBERS,)
    # I feared that somehow this method would give duplicated results... However, given how the puzzle is defined and the method I'm using here, it doesn't seem to be possible of grabbing the same gear set twice over the iterations.
    # Whatevs...

code.interact(local=locals())
