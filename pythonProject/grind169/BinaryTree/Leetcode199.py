import collections
from typing import Optional, List


# 199. Binary Tree Right Side View
# BFS,取最右邊的node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        res = []

        while queue:
            queue_len = len(queue)
            for i in range(queue_len):
                node = queue.popleft()
                if i == queue_len - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res





if __name__ == '__main__':
    result = Solution()
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    ans = result.rightSideView(root)
    print(ans)
