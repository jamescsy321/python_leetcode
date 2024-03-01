from typing import List


# 704. Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            elif nums[low] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1


if __name__ == '__main__':
    result = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    ans = result.search(nums, target)
    print(ans)
