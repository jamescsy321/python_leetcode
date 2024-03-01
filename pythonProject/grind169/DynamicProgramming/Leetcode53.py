from typing import List


# 53. Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum

    def maxSubArray2(self, nums: List[int]) -> int:
        max_sum = 0  # 最大和的初始值設定為負無窮
        curr_sum = 0
        for n in nums:
            curr_sum = max(curr_sum + n, n)
            max_sum = max(max_sum, curr_sum)
        return max_sum


if __name__ == '__main__':
    result = Solution()
