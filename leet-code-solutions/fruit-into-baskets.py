class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counter =defaultdict(int)
        left=0

        max_=0

        for right in range(len(fruits)):
            counter[fruits[right]]+=1
            
            while len(counter) > 2:
                if counter[fruits[left]] > 1:
                    counter[fruits[left]] -= 1
                else:
                    del counter[fruits[left]]
                left+=1
            max_=max(max_,right-left+1)
        
        return max_