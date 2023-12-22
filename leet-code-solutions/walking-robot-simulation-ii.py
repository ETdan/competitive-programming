class Robot:

    def __init__(self, width: int, height: int):
        self.directions=["East","North","West","South"]
        self.direction=0

        self.col=0
        self.row=0

        self.width=width
        self.height=height
    def step(self, num: int) -> None:
        # print(self.col,self.row)
        num %= (2*(self.width+self.height)-4)
        if self.col == 0 and self.row == 0:
            self.direction = 3
        while num:
            if self.direction == 0:
                # self.col = min(num,abs(self.width-self.col))
                # print(self.col, self.row, 'here')
                if self.col + num < self.width:
                    self.col += num
                    return
                else:
                    num -= self.width - self.col -1
                    self.col = self.width - 1
                    self.direction=1
                
            if self.direction == 1:
                if self.row + num < self.height:
                    self.row += num 
                    return
                else:
                    self.direction = 2
                    num -= self.height - 1 - self.row
                    self.row = self.height - 1 

            if self.direction == 2:
                if self.col >=  num:
                    # print(self.col, self.row,num, 'in dir')
                    self.col -= num
                    # print(self.col, self.row,num, 'in dir')
                    return
                else:
                    self.direction = 3
                    num -=  self.col 
                    self.col = 0

            if self.direction==3:
                if self.row >= num:
                    self.row -= num 
                    return
                else:
                    self.direction = 0
                    num -= self.row  
                    self.row = 0
            
        

    def getPos(self) -> List[int]:
        return [self.col,self.row]

    def getDir(self) -> str:
        return self.directions[self.direction]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()