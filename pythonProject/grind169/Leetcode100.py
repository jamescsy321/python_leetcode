from pythonProject.grind169 import TreeNode


def isSameTree(self, p, q):
    if p is None and q is None:
        return True
    if p is not None and q is not None:
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    return False


if __name__ == '__main__':
    p = TreeNode
    p.TreeNode(1).left(2)
    p.TreeNode(1).right(3)
    q = TreeNode
    q.TreeNode(1).left(2)
    q.TreeNode(1).right(3)


# isSameTree(p,q)
