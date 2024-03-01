from typing import List


# 349. Intersection of Two Arrays
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = []

        for num in nums1:
            low = 0
            high = len(nums2) - 1
            while low <= high:
                mid = (high - low) // 2 + low

                if num == nums2[mid] and num not in res:
                    res.append(num)
                    break
                elif nums2[mid] > num:
                    high = mid - 1
                else:
                    low = mid + 1
        return res


if __name__ == '__main__':
    result = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    nums3 = [4, 9, 5]
    nums4 = [9, 4, 9, 8, 4]
    ans = result.intersection(nums3, nums4)
    print(ans)
