class Solution:
    def hIndex(self, citations: List[int]) -> int:

        for i in range(len(citations)):
            # print(find_left_most_index(citations[i]))
            if citations[i] >= len(citations) - i:
                return len(citations) - i
        
        return 0 if citations[0] == 0 else 1