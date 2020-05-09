'''
Problem:
 Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters. 
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = list(s)
        b={}
        for i in a:
            if i in b.keys():
                b.update({i:b.get(i) + 1})
            else:
                b.update({i:1})
        if 1 not in b.values():
            return -1
        else:
            letter = list(b.keys())[list(b.values()).index(1)]
            return a.index(letter)