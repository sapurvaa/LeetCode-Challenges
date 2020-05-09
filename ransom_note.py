'''
Problem:
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        distinct_char = set(list(ransomNote))
        check_flag = "Yes"
        for i in distinct_char:
            if magazine.count(i) < ransomNote.count(i):
                check_flag = "No"
                break
            else:
                continue
        if check_flag == "No":
            return False
        else:
            return True
                            