'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
'''

#CODE

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        for digit in str(n):
            product *= int(digit)
            sum += int(digit)
        return product - sum
'''
Success Details:
Runtime: 39 ms, faster than 79.65% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
Memory Usage: 13.8 MB, less than 54.08% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
'''
