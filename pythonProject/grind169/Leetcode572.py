from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isMatch(self, s, t):
            if not s and t:
                return s is t
            return s.val == t.val and self.isMatch(s.left, t.left) and self.isMatch(s.right, t.right)

        if self.isMatch(root, subRoot):
            return True
        if not subRoot: return False
        return self.isSubtree(subRoot.left, root) or self.isSubtree(subRoot.right, root)
