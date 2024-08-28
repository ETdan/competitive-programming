# Problem: D - Decide Your Division - https://codeforces.com/gym/543431/problem/D

import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    while n > 1:
        if n % 5 == 0:
            n = (n*4) // 5
        elif n % 3 == 0:
            n = (n*2) // 3
        elif n % 2 == 0:
            n //= 2
        else:
            n = 0
        count += 1
    if n == 1:
        print(count)
    else:
        print(-1)
