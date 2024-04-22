# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        q = deque()

        if target not in visited:
            q.append(["0000",0])
        
        # bfs
        moves = float("inf")
        while q:
            length=len(q)
            # print(q)
            for _ in range(length):
                state,turn = q.popleft()

                if state == target:
                    # print(state,moves,"//////////")
                    moves = min(moves,turn)

                if state not in visited:
                    temp = state
                    visited.add(state)

                    # increment
                    for i in range(4):
                        # print("bb",i,temp)
                        digit = str((int(temp[i]) + 1) % 10)
                        temp1 = temp[:i] + digit + temp[i+1:]
                        # print("aaaap",digit,temp)
                        if temp1 not in visited:
                            q.append([temp1,turn+1])
                        
                        digit = str((int(temp[i]) - 1+10) % 10)
                        # print(int(temp[i]))
                        temp2 = temp[:i] + digit + temp[i+1:]
                        # print("aaaan",digit,temp)
                 
                        if temp2 not in visited:
                            q.append([temp2,turn+1])
                            # visited.add(temp)

                    # decrement
                    # for i in range(4):
                            # visited.add(temp)

        return moves if moves != float("inf") else -1