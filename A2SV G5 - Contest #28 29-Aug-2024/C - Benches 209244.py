# Problem: C - Benches - https://codeforces.com/gym/540354/problem/C

import sys
import math
input = sys.stdin.readline
t = int(input())
m = int(input())
km = m
arr = []
for _ in range(t):
    ai = int(input())
    arr.append(ai)

arr.sort()
max_ = arr[-1]
i = 0

while i < len(arr) and arr[i] <= max_ and m:
    if m > max_-arr[i]:
        m -= max_-arr[i]
    else:
        m = 0
    i += 1

min_ = max_+math.ceil(m / t)

print(min_, max_+km)
