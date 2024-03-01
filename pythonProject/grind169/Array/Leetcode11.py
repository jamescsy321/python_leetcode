from typing import List


# 11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_result = 0

        while left < right:
            min_number = min(height[left], height[right])
            dif = (right - left)
            water = min(height[left], height[right]) * (right - left)
            if water > max_result:
                max_result = water

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_result


if __name__ == '__main__':
    result = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    ans = result.maxArea(height)
    print(ans)
