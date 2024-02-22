class RecentCounter:

    def __init__(self):
        self.stack=deque()

    def ping(self, t: int) -> int:
        self.stack.append(t)
        while t - self.stack[0] >= 3001 :
            self.stack.popleft()

        # print(self.stack)
        return len(self.stack)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)