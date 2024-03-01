from typing import List


# 33. Search in Rotated Sorted Array33. Search in Rotated Sorted Array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = ( high-low ) // 2 + low

            if nums[mid] == target:
                return mid

            elif nums[low] < nums[mid]:
                if nums[low] == target:
                    return low
                elif nums[low] < target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[high] == target:
                    return high
                elif nums[mid] < target < nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


if __name__ == '__main__':
    result = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    ans = result.search(nums, target)
    print(ans)
