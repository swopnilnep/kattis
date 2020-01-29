# https://open.kattis.com/problems/chanukah
    
from sys import stdin

def series_sum(n : int):
    return int((n / 2) * (n + 1))

n = int( stdin.readline() )

for i in range(n):
    sno, days = str(stdin.readline()).split(' ')
    days = int(days)
    total = days + series_sum(days)
    print('{} {}'.format(sno , total))