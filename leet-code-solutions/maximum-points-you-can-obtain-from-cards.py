class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # start from left, right and decrease both values
        # number of itteration may be equal to k
        left=0
        right=k-1

        pre_sum=sum(cardPoints[:k])
        max_sum=pre_sum

        # print(pre_sum,len(cardPoints[:k]),cardPoints[:k])

        for _ in range(k):
            left-=1
            pre_sum+=cardPoints[left % len(cardPoints)]

            # remove right
            pre_sum-=cardPoints[right % len(cardPoints)]
            right-=1

            max_sum=max(max_sum,pre_sum)
            # print(max_sum)
        
        return max_sum