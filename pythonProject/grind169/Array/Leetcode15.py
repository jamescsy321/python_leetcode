from typing import List


# 15. 3Sum
# Array
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        length = len(nums)
        nums.sort()
        # 迴圈-2是因為至少要保留兩個位置左指標及右指標
        for i in range(length - 2):
            # 如果當前位置與前一位值相同就跳過
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            #     像中間靠攏
            left = i + 1
            right = length - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                # 因為排序過後從左到右數字由小到大，當小於0時代表數字要再更大，因此左指標要往右，當大於0時代表右指標要往左
                # ，等於0時便將三個數字放入result
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    # 結果為0就將內容放入result，之後將左指標極右指標位移一位並判斷是否位移後數字相同
                    result.append([nums[i], nums[left], nums[right]])
                    # 判斷左指標及右指標及旁邊數字是否相同，相同的話要再位移一格
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result
