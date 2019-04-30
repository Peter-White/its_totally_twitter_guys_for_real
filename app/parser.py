import re

def parse(s):
    p = re.compile('[A-Z][a-z]+\s[A-Z][a-zA-Z]+$')

    found = p.match(s)

    print(found)

    return found
