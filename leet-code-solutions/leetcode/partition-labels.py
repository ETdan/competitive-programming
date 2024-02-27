class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occ = defaultdict()
        answer = []
        for i in range(len(s)):
            last_occ[s[i]] = i

        curr_max = last_occ[s[0]]
        counter = 0

        for i in range(len(s)):
            if i < curr_max and last_occ[s[i]] > curr_max:
                curr_max = last_occ[s[i]]
            elif i > curr_max:
                answer.append(counter)
                curr_max = last_occ[s[i]]
                counter = 0
            counter += 1
        answer.append(counter)

        return answer
