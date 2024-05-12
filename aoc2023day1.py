import re, code

INPUT = open('INPUT.txt', 'r').read()
INPUT = '\n'+INPUT+'\n'

def group(term):
    return f"(?:{term})"

def oretup(wordtup):
    return f"(?:{'|'.join(tuple(group(e) for e in wordtup))})"

def ore(*args):
    return f"(?:{'|'.join(args)})"

def cgroup(term, groupname=''):
    return '('+term+')' if not groupname else f"(?P<{groupname}>{term})"

# Solves the text overlap issue
def lookahead(term):
    return r"(?="+term+")"

# double = r"(?:(?<=\n).*?____.*____.*?\n)"
# single = r"(?:(?<=\n).*?____.*?\n)"
digits = {
    "1"     : "1",
    "2"     : "2",
    "3"     : "3",
    "4"     : "4",
    "5"     : "5",
    "6"     : "6",
    "7"     : "7",
    "8"     : "8",
    "9"     : "9",
    "one"   : "1",
    "two"   : "2",
    "three" : "3",
    "four"  : "4",
    "five"  : "5",
    "six"   : "6",
    "seven" : "7",
    "eight" : "8",
    "nine"  : "9",
}

# This solution doesn't do well when strictly two and only 2 words of digits are overlapping
# part1 = ore(double.replace('____', r"(\d)"), single.replace('____', r"(\d)"))
# part2 = ore(double.replace('____', digit), single.replace('____', digit))

part1 = r"(\d)"
part2 = lookahead(cgroup(oretup(tuple(e for e in digits.keys() if len(e) > 1) + (r"\d", ))))

def answer(part):
    RE = re.compile(part, re.IGNORECASE)
    data = [RE.findall(e) for e in re.split(r"\n+", INPUT)]
    return sum([int(''.join((digits[e[0]], digits[e[-1]]))) for e in data if e])

code.interact(local=locals())
