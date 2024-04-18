# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        Dict = defaultdict(int)

        for word in words:
            Dict[word] += 1

        heap = []
        heapq.heapify(heap)

        for key, val in Dict.items():
            heapq.heappush(heap, (-val, key))

        answer = []
        while k and heap:
            answer.append(heapq.heappop(heap)[1])
            k-=1

        return answer
