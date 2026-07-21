from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Check every pair of numbers
        for i in range(len(nums)):

            # Compare the current number with the remaining numbers
            for j in range(i + 1, len(nums)):

                # If their sum equals the target
                if nums[i] + nums[j] == target:

                    # Return their indices
                    return [i, j]