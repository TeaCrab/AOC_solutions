import re, code
from math import prod

INPUT = open('INPUT.txt', 'r').read()
INPUT = '\n'+INPUT+'\n'

rawlist = re.split(r"[:;\n] *", INPUT.lower())

board = dict()
context = 1

for e in rawlist:
    match re.split(r'[, ] *', e):
        case ['game', number] :
            context = int(number)
            if context not in board.keys():
                board[context] = {'red':0, 'blue':0, 'green':0}
                continue
        case _ as content:
            content = [e for e in content if e != '']
            if len(content) > 0:
                board[context][content[1]] = max(int(content[0]), board[context][content[1]])
            if len(content) > 2:
                board[context][content[3]] = max(int(content[2]), board[context][content[3]])
            if len(content) > 4:
                board[context][content[5]] = max(int(content[4]), board[context][content[5]])
    pass

limit = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

keys = [key for key, value in board.items() if all([v <= limit[k] for k, v in value.items()])]

part1 = lambda: sum([key for key, value in board.items() if all([v <= limit[k] for k, v in value.items()])])
part2 = lambda: sum([prod([e for e in value.values()]) for value in board.values()])

code.interact(local=locals())
