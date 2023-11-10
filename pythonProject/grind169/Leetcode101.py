
from typing import Optional

from pythonProject.grind169 import TreeNode


def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if root is None:
        return True
    else:
        return self.isMirror(root.left, root.right)


def isMirror(self, left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if left.val == right.val:
        outPair = self.isMirror(left.left, right.right)
        inPiar = self.isMirror(left.right, right.left)
        return outPair and inPiar
    else:
        return False
