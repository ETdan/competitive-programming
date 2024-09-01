# Problem: C - InXtracting a Subsegment - https://codeforces.com/gym/537362/problem/C

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == 1:
    print(min(a))

elif k == 2:
    print(max(a[0], a[-1]))

else:
    print(max(a))
