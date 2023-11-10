from typing import List, Optional

from pythonProject.grind169 import TreeNode


#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 108. Convert Sorted Array to Binary Search Tree
def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    total_nums = len(nums)
    if not total_nums:
        return None

    mid_node = total_nums // 2
    return TreeNode(
        nums[mid_node],
        self.sortedArrayToBST(nums[:mid_node]), self.sortedArrayToBST(nums[mid_node + 1:])
    )


def sortedArrayToBST2(self, num):
    if not num:
        return None

    mid = len(num) // 2

    root = TreeNode(num[mid])
    root.left = self.sortedArrayToBST(num[:mid])
    root.right = self.sortedArrayToBST(num[mid + 1:])

    return root

# sortedArrayToBST2(self, num) 是一個方法，它接受一個已排序的數組 num 作為參數，並返回一棵二分查找樹的根節點。
# 首先，程式檢查 num 是否為空（空數組）。如果 num 為空，則返回 None，因為空數組無法構建BST。
# 程式計算數組的中間元素，這個中間元素將成為BST的根節點。這是通過 mid = len(num) // 2 來實現的。
# 接下來，程式創建一個新的 TreeNode 物件，將中間元素 num[mid] 作為根節點的值。
# 然後，程式遞迴調用 sortedArrayToBST 方法兩次，分別處理左子樹和右子樹。對於左子樹，它遞迴調用 sortedArrayToBST，傳入 num[:mid]，
# 這表示取數組中從頭到中間（不包括中間）的部分。對於右子樹，它遞迴調用 sortedArrayToBST，傳入 num[mid + 1:]，這表示取數組中從中間+1到結尾的部分。
# 最後，將左子樹和右子樹連接到根節點上，並返回根節點。
