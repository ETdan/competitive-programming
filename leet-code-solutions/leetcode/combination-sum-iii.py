class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [num for num in range(1,10)]
        answer = []
        temp = []
        seen = set()

        def recur(left):
            nonlocal seen
            
            if temp and tuple(sorted(temp)) in seen:
                return
            
            if len(temp) > k:
                return

            seen.add(tuple(sorted(temp)))

            sum_ = sum(temp)
            if sum_ == n and len(temp) == k:
                answer.append(temp[:])
                return
            elif sum_ > n:
                return

            for i in range(left, len(candidates)):
                temp.append(candidates[i])
                recur(i + 1)
                temp.pop()

        recur(0)
        return answer
