from typing import List


# 560. Subarray Sum Equals K
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sub_sum = 0
        lookup = {0: 1}

        for num in nums:
            curr_sub_sum += num

            if curr_sub_sum - k in lookup:
                count += lookup[curr_sub_sum - k]

            lookup[curr_sub_sum] = lookup.get(curr_sub_sum, 0) + 1

        return count


if __name__ == '__main__':
    result = Solution()
    nums = [3, 4, 7, 2, -3, 1, 4, 2]
    k = 7
    ans = result.subarraySum(nums, k)
    print(ans)
