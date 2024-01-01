class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        max_=0

        for i in range(len(processorTime)):
            temp=0
            for j in range(i*4,i*4+4):
                temp=max(temp,processorTime[i]+tasks[j])
                # print(processorTime[i],tasks[j])
            max_=max(max_,temp)

        return max_