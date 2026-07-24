#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

#The overall run time complexity should be O(log (m+n)).
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:

            partitionX = (left + right) // 2
            partitionY = (m + n + 1) // 2 - partitionX

            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == m else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == n else nums2[partitionY]

            # Correct partition found
            if maxLeftX <= minRightY and maxLeftY <= minRightX:

                # Odd number of elements
                if (m + n) % 2 == 1:
                    return max(maxLeftX, maxLeftY)

                # Even number of elements
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2

            # Move binary search left
            elif maxLeftX > minRightY:
                right = partitionX - 1

            # Move binary search right
            else:
                left = partitionX + 1