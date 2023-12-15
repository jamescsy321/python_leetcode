from typing import List


# 977. Squares of a Sorted Array
# 平方列表內的所有值並且排序
def sortedSquares(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        nums[i] *= nums[i]
    nums.sort()
    return nums


def sortedSquares2(nums: List[int]) -> List[int]:
    # num**2 计算了 num 的平方最後在排序並回傳一個新的列表
    return sorted([num ** 2 for num in nums])


if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    result = sortedSquares(nums)
    print(result)
