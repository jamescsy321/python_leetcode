from typing import List


# 525. Contiguous Array
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        hash = {}
        count = 0
        for i in range(len(nums)):
            current = nums[i]
            if current == 0:
                count -= 1
            else:
                count += 1

            if count == 0:
                max_length = i + 1
            if count in hash:
                max_length = max(max_length, i - hash[count])
            else:
                hash[count] = i
        return max_length


if __name__ == '__main__':
    result = Solution()
    nums = [0, 1, 0, 0, 0, 1, 1, 0, 1]
    ans = result.findMaxLength(nums)
    print(ans)
