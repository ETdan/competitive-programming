# Problem: A - Duale String - https://codeforces.com/gym/520688/problem/A

from sys import stdin, stdout, setrecursionlimit
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    s = input().strip()
    if 2*s[:len(s)//2] == s:
        print("YES")
    else:
        print("NO")
