'''
Problem:

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true

Example 2:

Input: 14
Output: false
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        else:
            low = 1
            high=num//2
            while low <= high:
                mid = (low+high)//2
                if mid*mid == num:
                    return True
                else:
                    if mid*mid > num:
                        high = mid-1
                    else:
                        low = mid+1
            return False