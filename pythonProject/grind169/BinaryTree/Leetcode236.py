# 236. Lowest Common Ancestor of a Binary Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return

        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if left:
            return left
        if right:
            return right


if __name__ == '__main__':
    result = Solution()
    # tree = TreeNode(3)
    # tree.left = TreeNode(5)
    # tree.right = TreeNode(1)
    # tree.left.left = TreeNode(6)
    # tree.left.right = TreeNode(2)
    # tree.left.right.left = TreeNode(7)
    # tree.left.right.right = TreeNode(4)
    # tree.right.left = TreeNode(0)
    # tree.right.right = TreeNode(8)
    tree = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
    p = TreeNode(5)
    q = TreeNode(1)
    ans = result.lowestCommonAncestor(tree, p, q)
    print(ans)
