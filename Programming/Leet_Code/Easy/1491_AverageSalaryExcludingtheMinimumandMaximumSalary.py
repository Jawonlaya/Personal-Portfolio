'''
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
Example 2:

Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
'''

class Solution:
    def average(self, salary: List[int]) -> float:
        
        max_salary = max(salary)
        
        min_salary = min(salary)
        
        salary_sum = 0
        count = 0
        for s in salary:
            if s != min_salary and s != max_salary:
                salary_sum += s
                count += 1
                
        
        return salary_sum / count 
'''      
Output Result:Accepted
Runtime: 61 ms
Your input
[4000,3000,1000,2000]
Output
2500.00000
Expected
2500.00000
'''
