class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        answer=digits[::-1]
        answer.append(0)
        print(*answer)
        answer[0]+=1
        for i in range(len(answer)-1):
            if answer[i] == 10:
                answer[i]=0
                answer[i+1]+=1

        answer=answer[::-1]
        if answer[0] == 0:
            return answer[1:]
        return answer