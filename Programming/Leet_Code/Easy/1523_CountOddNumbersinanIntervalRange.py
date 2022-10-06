"""
    Given two non-negative integers low and high. Return the count of odd 
    numbers between low and high (inclusive).

    Example:
    Input: low = 3, high = 7
    Output: 3
    Explanation: The odd numbers between 3 and 7 are [3,5,7].

    Constraints:
        - 0 <= low <= high <= 10^9
"""

#Difficulty: Easy
#Runtime: 58 ms, faster than 28.40% of Python3 online submissions for Count Odd Numbers in an Interval Range.
#Memory Usage: 13.9 MB, less than 59.14% of Python3 online submissions for Count Odd Numbers in an Interval Range.

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        if low % 2 != 0:
            if high % 2 != 0:
                return (high - low) // 2 + 1
            else:
                return (high - low) // 2 + 1
        else:
            if high % 2 != 0: 
                return (high - low) // 2 + 1
            else: 
                return (high - low) // 2
