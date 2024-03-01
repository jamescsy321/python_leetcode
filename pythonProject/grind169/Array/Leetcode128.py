from typing import List


# 128. Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                longest = max(longest, length)
        return longest

    def longestConsecutive2(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0

        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best


if __name__ == '__main__':
    result = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    ans = result.longestConsecutive2(nums)
    print(ans)
