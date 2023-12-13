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


def twoSum2(nums: List[int], target: int) -> List[int]:
    #  初始一個map
    result_map = {}
    n = len(nums)
    for i in range(n):
        # 算出差異值
        dif = target - nums[i]
        # 如果差異值沒有在map中代表沒有配對到，因此要將數值及index位置存入map中
        # 將數值存成key，index位置存value，當有發現差異值在map，
        # 就可以將map中的key值對應的value取出跟目前的index回傳為解答
        if dif in result_map:
            return [result_map[nums[dif]], i]

        result_map[nums[i]] = i

    return []


if __name__ == '__main__':
    nums = [2, 12, 11, 7]
    target = 9
    result = twoSum2(nums, target)
    print(result)
