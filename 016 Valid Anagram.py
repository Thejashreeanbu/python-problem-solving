#Given two strings s and t, return True if t is an anagram of s, and False otherwise.

#An anagram is a word or phrase formed by rearranging the letters of another word, using all the original letters exactly once.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count:
                return False

            count[char] -= 1

            if count[char] < 0:
                return False

        return True