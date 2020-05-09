'''
Problem:
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = {}
        for i in nums:
            if i in unique.keys():
                unique.update({i:unique.get(i)+1})
            else:
                unique[i] = 1
        if 1 in unique.values():
            return list(unique.keys())[list(unique.values()).index(1)]