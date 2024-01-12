class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count_of_T = 0
        count_of_F = 0
        
        left = 0
        max_count=0

        # if count_of_T >= count_of_F:

        for right in range(len(answerKey)):
            if answerKey[right] == "T":
                count_of_T += 1
            else:
                count_of_F += 1
            
            if min(count_of_F,count_of_T) > k:
                if answerKey[left] == "T":
                    count_of_T -= 1
                else:
                    count_of_F -= 1

                left+=1
            # print(answerKey[left:right],max_count)
            max_count=max(max_count,right-left+1)

        return max_count

            

