import math
from typing import List


# 16. 3Sum Closest
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = math.inf

        for i in range(len(nums) - 1):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if abs(target - curr_sum) < abs(diff):
                    diff = target - curr_sum
                if diff == 0:
                    return target
                if curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return target - diff


if __name__ == '__main__':
    result = Solution()
    nums = [-1, 2, 1, -4]

    target = 1
    ans = result.threeSumClosest(nums, target)
    print(ans)
