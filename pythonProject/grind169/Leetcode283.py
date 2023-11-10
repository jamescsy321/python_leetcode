from typing import List


def moveZeroes(nums: List[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0 and nums[slow] == 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]

        if nums[slow] != 0:
            slow += 1


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    moveZeroes(nums)
    print(nums)

# slow 和 fast 是兩個變數，它們分別用於追蹤慢指針和快指針。一開始，它們都指向列表的開頭。
#
# 函數使用一個 for 迴圈來遍歷列表 nums 中的每個元素，其中 fast 是快指針，它不斷遞增，而 slow 是慢指針，它只在特定條件下遞增。
#
# 在每次迭代中，程式檢查 nums[fast] 是否不等於零並且 nums[slow] 是否等於零。如果這兩個條件都成立，表示我們找到了一個非零元素和一個零元素，需要將它們交換位置，以確保非零元素繼續保持在前面。
#
# 最後，如果 nums[slow] 不等於零，表示慢指針指向一個非零元素，所以將慢指針 slow 遞增。
#
# 這個過程將持續運行，直到快指針 fast 遍歷完整個列表 nums。最終的結果是所有的非零元素都在列表的前面，所有的零元素都在列表的後面，且它們的相對順序保持不變。
