# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def dijkstra(self,graph, start_node):
        distances = {node: float('inf') for node in graph}
        distances[start_node] = 0
        processed = set()

        heap = [(0, start_node)]
        while heap:
            p_distance,node = heapq.heappop(heap)
            if node in processed:
                continue

            processed.add(node)
            
            for child,distance in graph[node]:
                distances[child]=min(distances[child],distance+p_distance)
                heapq.heappush(heap,(distances[child],child))
        
        max_dis=0
        
        for key,val in distances.items():
            max_dis=max(max_dis,val)
        
        return max_dis
    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        for i in range(1,n+1):
            if i not in graph:
                graph[i]=[]
        answer = self.dijkstra(graph,k)
        return answer if answer != float('inf') else -1