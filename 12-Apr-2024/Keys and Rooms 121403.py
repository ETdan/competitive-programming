# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        can_visit=[False] * len(rooms)
        visited =set()

        q = deque()
        q.append(0)
        
        while q:
            for i in range(len(q)):
                index = q.popleft()
                if index not in visited:
                    visited.add(index)
                    can_visit[index]=True
                    q.extend(rooms[index])

        can_visit = set(can_visit)
        return len(can_visit) <= 1