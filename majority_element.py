'''
Problem:
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        for i in nums:
            if i not in count_dict.keys():
                count_dict[i] = 1
            else:
                count_dict.update({i:count_dict.get(i)+1})
        n = list(count_dict.keys())[list(count_dict.values()).index(max(list(count_dict.values())))]
        return n