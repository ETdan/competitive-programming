# Problem: D - Maximum Number of Zeroes - https://codeforces.com/gym/514644/problem/D

from collections import defaultdict
from math import gcd
import sys

input = sys.stdin.readline
Dict = defaultdict(int)

t = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

counter = 0

for i in range(len(a)):
    if a[i] == 0 and b[i] == 0:
        counter += 1
    elif a[i]:
        if b[i]:
            GCD = gcd(a[i], b[i])
            a[i] //= GCD
            b[i] //= GCD

            # print(a[i], b[i])

            if a[i] < 0 and b[i] < 0:
                Dict[(str(abs(a[i])) + '/'+str(abs(b[i])))] += 1
                # print("here 1")
            elif a[i] < 0 or b[i] < 0:
                # print("here")
                Dict[(str(0-abs(a[i])) + '/'+str(abs(b[i])))] += 1
            else:
                Dict[(str(a[i]) + '/'+str(b[i]))] += 1
        else:
            Dict["0"] += 1


max_ = 0
for val in Dict.values():
    max_ = max(max_, val)

print(max_ + counter)
# print(Dict)