from typing import List


# 189. Rotate Array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        demo = nums[:k]
        demo2 =nums[k:]
        nums[:k], nums[k:] = nums[len(nums) - k:], nums[:len(nums) - k]
        # n = len(nums)
        # k = k % n
        # nums[:] = nums[n-k:] + nums[:n-k]


if __name__ == '__main__':
    result = Solution()

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    result.rotate(nums, k)
    print(nums)
