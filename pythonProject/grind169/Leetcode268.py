from typing import List


# 用高斯求和公式 n * (n + 1) / 2 來計算 0 到 n 之間所有數字的總和。
# 使用 sum(nums) 來計算 nums 列表中所有數字的總和。
# 最後，它將高斯求和的結果減去 nums 列表的總和，這將得到缺失的數字。
def missingNumber(nums: List[int]) -> int:
    n = len(nums)
    return n * (n + 1) / 2 - sum(nums)


if __name__ == '__main__':
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    result = missingNumber(nums)
    print(result)
