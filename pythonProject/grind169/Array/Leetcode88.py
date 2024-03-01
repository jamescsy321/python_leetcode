from typing import List


# 88. Merge Sorted Array
# three pointer
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pointer_a = m - 1
        pointer_b = n - 1
        last = m + n - 1

        while pointer_a >= 0 and pointer_b >= 0:
            if nums1[pointer_a] > nums2[pointer_b]:
                nums1[last] = nums1[pointer_a]
                pointer_a -= 1
            else:
                nums1[last] = nums2[pointer_b]
                pointer_b -= 1
            last -= 1

        while pointer_b >= 0:
            nums1[last] = nums2[pointer_b]
            pointer_b -= 1
            last -= 1


if __name__ == '__main__':
    result = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    result.merge(nums1, m, nums2, n)
    print(nums1)
