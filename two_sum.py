'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:    
    def twoSum(self, nums, target):
        a = []
        for i in range(len(nums)):
            num_sum = target - nums[i]
            if num_sum in nums and nums.index(num_sum) != i:
                a = [i,nums.index(num_sum)]
                break
        if len(a) == 0:
            print("no two sum solution")
            return a
        else:
            print(a)
            return a