# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline
 
 
def dijkstar(graph):
    distances = {node: float('inf') for node in graph}
    distances[1] = 0
    heap = [(0, 1)]
    processed = set()
 
    while heap:
        curr_distance, curr_node = heapq.heappop(heap)
        if curr_node in processed:
            continue
 
        processed.add(curr_node)
 
        for child, weight in graph[curr_node]:
            distance = curr_distance + weight
            if distance < distances[child]:
                distances[child] = distance
                heapq.heappush(heap, (distance, child))
 
    return distances
 
 
n, m = list(map(int, (input().split())))
arr = set()
graph = defaultdict(list)
for _ in range(m):
    u, v = list(map(int, (input().split())))
    arr.add((u, v))
 
if (1, n) not in arr and (n, 1) not in arr:
    # print('here')
    for u, v in arr:
        graph[u].append((v, 1))
        graph[v].append((u, 1))
 
else:
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if (i, j) not in arr and (j, i) not in arr:
                graph[i].append((j, 1))
                graph[j].append((i, 1))
 
 
# print(graph)
answer = dijkstar(graph)
if n not in answer or answer[n] == float('inf'):
    print(-1)
else:
    print(answer[n])
 
# print(arr)