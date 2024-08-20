# Problem: A - Split the Set - https://codeforces.com/gym/538762/problem/A

import sys
input = lambda: sys.stdin.readline().rstrip()


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    odd_count = 0
    even_count = 0

    for num in a:
        if num & 1:
            odd_count += 1
        else:
            even_count += 1

    print('Yes' if odd_count == even_count else 'No')