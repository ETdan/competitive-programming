# Problem: B - Diversity - https://codeforces.com/gym/543431/problem/B

import sys
from collections import Counter
input = sys.stdin.readline
s = input().strip()
k = int(input())
length = len(s)

uniq = Counter(s)
count = 0
for key, val in uniq.items():
    if val == 1:
        count += 1
if length < k or k > 26:
    print("impossible")
else:
    dif = set(s)
    if len(dif) >= k:
        print(0)
    else:
        print(k-len(dif))
