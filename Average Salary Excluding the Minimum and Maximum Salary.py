class Solution:
    def average(self, salary: List[int]) -> float:
        return 1.0*(sum(salary)-max(salary)-min(salary))/(len(salary)-2)
