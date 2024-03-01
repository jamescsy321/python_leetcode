from typing import List


# 153. Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

if __name__ == '__main__':
    result = Solution()
    nums = [3, 4, 5, 1, 2]
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    ans = result.findMin(nums2)
    print(ans)
