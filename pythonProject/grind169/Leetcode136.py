from typing import List


# 位異或運算 兩個相同值異或後為0
# 因此，如果数组中的某个元素只出现一次，而其他元素都出现两次，最终 ans 中将只剩下那个只出现一次的元素，因为出现两次的元素都被抵消了
def singleNumber(nums: List[int]) -> int:
    ans = 0
    for num in nums:
        ans ^= num

    return ans


if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2]
    result = singleNumber(nums)
    print(result)
