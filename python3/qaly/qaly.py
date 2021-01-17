# Quality of life lived, (0,1)
from sys import stdin
periods, qaly = int(stdin.readline()), 0
multiply = (lambda x,y: x * y)
while periods > 0:
    qaly += multiply(*(float(x) for x in stdin.readline().strip().split()))
    periods -= 1
print(qaly)