# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        def dijkstar(graph):
            distances = {node: float('inf') for node in graph}
            distances[start_node] = 0
            processed = set()
            heap = [(1, start_node)]

            while heap:
                current_distance, current_node = heapq.heappop(heap)
                if current_node in processed:
                    continue
                processed.add(current_node)

                for child, weight in graph[current_node]:
                    distance = current_distance * weight
                    
                    if distance > 0:
                        distance*=-1

                    # print(distance,distances[child],child,current_node)
                    if distance < distances[child]:
                        distances[child] = distance
                        heapq.heappush(heap, (distance, child))
            
            # print(distances)
            return distances[end_node]

        graph = defaultdict(list)

        for i in range(len(edges)):
            u,v = edges[i]
            w=succProb[i]
            graph[u].append((v,-w))
            graph[v].append((u,-w))
        
        for i in range(n):
            if i not in graph:
                graph[i]=[]
        
        answer = dijkstar(graph)

        return -answer if answer != float('inf') else 0
                