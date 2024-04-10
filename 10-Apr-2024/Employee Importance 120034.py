# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        queue = [id]
        directory = {}
        for e in employees:
            directory[e.id] = e

        total = 0
    
        while queue:
            emp_id = queue.pop()
            emp = directory[emp_id]
            total += emp.importance

            for sub in emp.subordinates:
                queue.append(sub)

        return total