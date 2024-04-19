# Problem: Productive Meeting - https://codeforces.com/contest/1579/problem/D

import heapq
import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    min_heap = list(map(int, input().split()))

    max_heap = [(-num, index)
                for index, num in enumerate(min_heap) if num != 0]

    heapq.heapify(max_heap)

    k = 0
    answer = []

    while len(max_heap) > 1:
        num1 = heapq.heappop(max_heap)
        num2 = heapq.heappop(max_heap)

        k += 1
        answer.append((num1[1]+1, num2[1]+1))

        if num1[0] + 1 != 0:
            heapq.heappush(max_heap, (num1[0]+1, num1[1]))

        if num2[0] + 1 != 0:
            heapq.heappush(max_heap, (num2[0]+1, num2[1]))

    print(k)
    for i in range(len(answer)):
        print(*answer[i])
