from sys import stdin
for n in stdin.readlines():  
    n = int(n.strip() )
    l1, l2 = [], []
    for i in range(1, int(n ** 0.5) + 1):
        q,r = n//i, n%i     # Alter: divmod() fn can be used.
        if r == 0:
            l1.append(i) 
            l2.append(q)    # q's obtained are decreasing.
    if l1[-1] == l2[-1]:    # To avoid duplication of the possible factor sqrt(n)
        l1.pop()
    l2.reverse()
    sf = sum((l1 + l2)[:-1])
    if sf == n:
        print(str(n) + ' perfect')
    elif abs(n - sf) <= 2:
        print(str(n) + ' almost perfect')
    else:
        print(str(n) + ' not perfect')