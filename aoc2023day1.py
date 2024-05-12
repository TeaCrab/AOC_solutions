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

double = r"(?:(?<=\n).*?____.*____.*?\n)"
single = r"(?:(?<=\n).*?____.*?\n)"
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

digit = cgroup(oretup(tuple(e for e in digits.keys() if len(e) > 1) + (r"\d", )))

part1 = ore(double.replace('____', r"(\d)"), single.replace('____', r"(\d)"))
part2 = ore(double.replace('____', digit), single.replace('____', digit))

def answer(part):
    RE = re.compile(part, re.IGNORECASE)
    data = RE.findall(INPUT)
    data = [[e for e in tup if e!=''] for tup in data]
    data = [e * int(2 // len(e)) for e in data]
    func = lambda tup: int(''.join([digits[e] for e in tup]))
    return sum([func(tup) for tup in data])

code.interact(local=locals())
