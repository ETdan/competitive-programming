class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        left=0
        counter=defaultdict(int)

        k_counter=0
        k_minus_1_counter=0

        for right in range(len(nums)):
            counter[nums[right]] += 1
            while len(counter) > k:
                if counter[nums[left]] > 1:    
                    counter[nums[left]] -= 1
                else:
                    del counter[nums[left]]
                left+=1

            k_counter += right-left+1

        left=0
        counter=defaultdict(int)
        
        for right in range(len(nums)):
            counter[nums[right]] += 1
            while len(counter) > k-1:
                if counter[nums[left]] > 1:    
                    counter[nums[left]] -= 1
                else:
                    del counter[nums[left]]
                left+=1

            k_minus_1_counter += right-left+1

        return k_counter - k_minus_1_counter

    # what we did here is we first calculated for <=k then <=k-1 when we substruct k-1 from k we get for exactly k
