#You are given an integer array nums of length n and an integer target.

#Find three integers at distinct indices in nums such that the sum is closest to target.

#Return the sum of the three integers.

#You may assume that each input would have exactly one solution.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest=float('inf')
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                current_sum=nums[i]+nums[left]+nums[right]
                if abs(current_sum-target)<abs(closest-target):
                    closest=current_sum
                if current_sum<target:
                    left+=1
                elif current_sum>target:
                    right-=1
                else:
                    return current_sum
        return closest
        