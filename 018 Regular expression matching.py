#Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

#'.' Matches any single character.​​​​
#'*' Matches zero or more of the preceding element.
#Return a boolean indicating whether the matching covers the entire input string (not partial).
#Example 1:
#Input: s = "aa", p = "a"
#Output: false
#Explanation: "a" does not match the entire string "aa".
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            first_match = (
                i < len(s) and
                (s[i] == p[j] or p[j] == '.')
            )

            if j + 1 < len(p) and p[j + 1] == '*':
                result = (
                    dfs(i, j + 2) or
                    (first_match and dfs(i + 1, j))
                )
            else:
                result = first_match and dfs(i + 1, j + 1)

            memo[(i, j)] = result
            return result

        return dfs(0, 0)