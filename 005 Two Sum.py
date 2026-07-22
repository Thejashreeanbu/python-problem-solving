
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

#explain this question

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Check every pair of numbers
        for i in range(len(nums)):

            # Compare the current number with the remaining numbers
            for j in range(i + 1, len(nums)):

                # If their sum equals the target
                if nums[i] + nums[j] == target:

                    
                    return [i, j]