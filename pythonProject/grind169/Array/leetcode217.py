from typing import List


# 217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        num_set = set(nums)
        return len(set(nums)) != len(nums)


if __name__ == '__main__':
    result = Solution()
    nums_1 = [1, 2, 3, 1]
    nums_2 = [1, 2, 3, 4]
    nums_3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    ans = result.containsDuplicate2(nums_1)
    print(ans)
