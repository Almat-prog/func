from functools import reduce
def is_palindreome(s):
    s = list(filter(lambda c: c.isalnum (),s.lower()))
    return reduce(lambda x, y: x and y, map(lambda x, y: x == y, s, reversed(s)), True)
print(is_palindreome("kazak"))
print(is_palindreome("hele"))