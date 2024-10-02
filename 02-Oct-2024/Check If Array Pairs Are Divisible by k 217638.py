# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        Dict = defaultdict(int)
        count_of_zero = 0

        for i in range(len(arr)):
            if arr[i] % k == 0:
                count_of_zero += 1
            else:
                if k - (arr[i] % k) in Dict and Dict[k - (arr[i] % k)] > 0:
                    Dict[k - (arr[i] % k)] -= 1
                else:
                    Dict[arr[i] % k] += 1

        # print(Dict)
        for key,val in Dict.items():
            if val != 0:
                return False

        return count_of_zero % 2 == 0