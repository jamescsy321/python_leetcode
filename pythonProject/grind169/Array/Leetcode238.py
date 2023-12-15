from typing import List


# LeetCode 238. Product of Array Except Self
# Array
"""
nums=[1, 2, 3, 4]
ans =[24,12,8, 6]
24  =    2* 3* 4
12  = 1*  * 3* 4
8   = 1*2*     4
6   = 1*2* 3

left =[1, 1, 2, 6]
right=[24,12,4, 1]
ans  =[24,12,8,6]

"""
class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)
        left, right, answer = [0] * length, [0] * length, [0] * length
        left[0] = 1
        for i in range(1, length):
            left[i] = nums[i - 1] * left[i - 1]
        right[length - 1] = 1

        for i in reversed(range(length - 1)):
            right[i] = nums[i + 1] * right[i + 1]

        for i in range(length):
            answer[i] = left[i] * right[i]

        return answer

if __name__ == '__main__':
    result = Solution()
    question = [1,2,3,4]
    ans = result.productExceptSelf(question)
    print(ans)
