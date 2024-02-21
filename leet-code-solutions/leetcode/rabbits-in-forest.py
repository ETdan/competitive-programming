class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count_dict=defaultdict(int)
        
        for answer in answers:
            count_dict[answer]+=1
        tot_num_of_rabit=0

        for key,val in count_dict.items():
            tot_num_of_rabit+=((ceil(val/(key+1)))*(key+1))

        return tot_num_of_rabit