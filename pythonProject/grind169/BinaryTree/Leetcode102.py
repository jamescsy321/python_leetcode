import collections
from typing import List, Optional


# 102. Binary Tree Level Order Traversal
# Definition for a binary tree node.
# 解tree題目兩種技巧BFS/DFS，這題使用BFS
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = collections.deque()
        queue.append(root)

        while queue:
            queue_len = len(queue)
            curr_list = []
            for _ in range(queue_len):
                node = queue.popleft()
                curr_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(curr_list)

        return result


if __name__ == '__main__':
    result = Solution()
    tree = TreeNode(3, TreeNode(9, None), TreeNode(20, TreeNode(15), TreeNode(7)))
    ans = result.levelOrder(tree)
    print(ans)
