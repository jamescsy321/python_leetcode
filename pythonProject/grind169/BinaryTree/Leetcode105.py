from typing import List, Optional


# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root_value = preorder[0]
        root = TreeNode(root_value)
        inorder_index = inorder.index(root_value)

        root.left = self.buildTree(preorder[1:inorder_index + 1], inorder[:inorder_index])
        root.right = self.buildTree(preorder[inorder_index + 1:], inorder[inorder_index + 1:])

        return root


if __name__ == '__main__':
    result = Solution()
    # preorder 前序遍歷, inorder 中序遍歷
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    ans = result.buildTree(preorder, inorder)
    print(ans)
