import math
from typing import List


# 209. Minimum Size Subarray Sum
# sliding window
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_length = 0
        output = math.inf
        curr_sum = 0
        start = 0

        for end in range(len(nums)):
            curr_sum += nums[end]
            curr_length += 1

            while curr_sum >= target:
                output = min(output, curr_length)
                curr_sum -= nums[start]
                start += 1
                curr_length -= 1

        if output == math.inf:
            return 0

        return output


if __name__ == '__main__':
    result = Solution()
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    ans = result.minSubArrayLen(target, nums)
    print(ans)
