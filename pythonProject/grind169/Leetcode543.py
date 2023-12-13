from typing import Optional


# 543. Diameter of Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def find_diameter(node):
            if not node:
                return 0

            left = find_diameter(node.left)
            right = find_diameter(node.right)

            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)

        find_diameter(root)
        return self.diameter


if __name__ == '__main__':
    result = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    ans = result.diameterOfBinaryTree(root)
    print(ans)
