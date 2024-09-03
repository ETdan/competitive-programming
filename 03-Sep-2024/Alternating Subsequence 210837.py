# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

import sys
input = sys.stdin.readline


def sign(a, b):
    if (a < 0 and b < 0) or (a > 0 and b > 0):
        return True

    return False


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    i = 0
    sum = 0
    while i < len(arr):
        curr = arr[i]
        j = i
        while j < len(arr) and sign(arr[j], arr[i]):
            curr = max(curr, arr[j])
            j += 1

        sum += curr
        i = j

    print(sum)
