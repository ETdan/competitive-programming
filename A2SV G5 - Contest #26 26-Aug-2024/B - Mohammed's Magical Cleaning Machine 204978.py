# Problem: B - Mohammed's Magical Cleaning Machine - https://codeforces.com/gym/537362/problem/B

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    counter = 0
    found_num = False
    for i in range(n-1):
        if arr[i] == 0 and found_num:
            counter += 1
        elif arr[i] > 0:
            found_num = True
            counter += arr[i]
    print(counter)
