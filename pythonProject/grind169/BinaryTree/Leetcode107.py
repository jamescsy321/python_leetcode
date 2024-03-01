import collections
from typing import Optional, List


# 107. Binary Tree Level Order Traversal II
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = collections.deque()
        queue = collections.deque()
        queue.append(root)

        while queue:
            curr_list = []
            queue_len = len(queue)

            for _ in range(queue_len):
                node = queue.popleft()
                curr_list.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.appendleft(curr_list)
        return res


if __name__ == '__main__':
    result = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    ans = result.levelOrderBottom(root)
    print(ans)
