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
        idIndex = {}
        
        for i, employee in enumerate(employees):
            idIndex[employee.id] = i

        def dfs(employee, visited):
            if not employee:
                return 0

            total = employee.importance
            visited.add(employee.id)

            for subordinate in employee.subordinates:
                if subordinate not in visited:
                    total += dfs(employees[idIndex[subordinate]], visited)

            return total
        
        for employee in employees:
            if employee.id == id:
                return dfs(employee, set())
        
    
