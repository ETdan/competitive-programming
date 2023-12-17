class ATM:

    def __init__(self):
        self.holder=[20,50,100,200,500]
        self.notes=[0]*5    

    def deposit(self, banknotesCount: List[int]) -> None:
        self.notes[0] += banknotesCount[0]
        self.notes[1] += banknotesCount[1]
        self.notes[2] += banknotesCount[2]
        self.notes[3] += banknotesCount[3]
        self.notes[4] += banknotesCount[4]

    def withdraw(self, amount: int) -> List[int]:
        answer=[0]*5
        
        for i in range(len(self.holder)-1,-1,-1):
            used=min(amount // self.holder[i],self.notes[i])
            answer[i]+=used
            amount-=used*self.holder[i]

        if amount == 0:
            for i in range(5):
                self.notes[i] -=  answer[i]
            
            return answer
        else:
            return [-1]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)