from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def twoSumWithHashTable(nums: List[int], target: int) -> List[int]:
    num_map = {}
    n = len(nums)

    for i in range(n):
        number = target - nums[i]
        if number in num_map:
            return [num_map[number], i]
        num_map[nums[i]] = i
    return []


if __name__ == '__main__':
    nums = [2, 12, 11, 7]
    target = 9
    result = twoSumWithHashTable(nums, target)
    print(result)


