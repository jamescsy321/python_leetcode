from typing import List


# 169. Majority Element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        index, count = 0, 1

        for i in range(1, len(nums)):
            if nums[index] == nums[i]:
                count += 1
            else:
                count -= 1
                
                if count == 0:
                    index = i
                    count = 1
        return nums[index]


if __name__ == '__main__':
    result = Solution()
    nums = [3, 2, 3]
    nums_two = [2, 2, 1, 1, 1, 2, 2]
    ans = result.majorityElement(nums)
    print(ans)
