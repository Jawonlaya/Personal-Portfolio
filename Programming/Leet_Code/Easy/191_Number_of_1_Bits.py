'''
Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
 

Example 1:

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
'''

# CODE
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while(True):
            if n==0:
                break
            if n & 1 == 1: #check for the last bit 
                count +=1
            n = int(n/2)
        return count 



'''
Success Details: 
Runtime: 32 ms, faster than 94.02% of Python3 online submissions for Number of 1 Bits.
Memory Usage: 13.9 MB, less than 49.74% of Python3 online submissions for Number of 1 Bits.
'''
