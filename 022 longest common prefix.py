#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".

 

#Example 1:

#Input: strs = ["flower","flow","flight"]
#Output: "fl"
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix