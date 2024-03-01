import collections
from typing import Optional, List


# 103 Binary Tree Zigzag Level Order Traversal
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = collections.deque()
        result = []
        queue.append(root)
        normal_append = True

        while queue:
            quene_len = len(queue)
            curr_list = collections.deque()

            for _ in range(quene_len):
                node = queue.popleft()
                if normal_append:
                    curr_list.append(node.val)
                else:
                    curr_list.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(curr_list)
            normal_append = not normal_append

        return result


if __name__ == '__main__':
    result = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    ans = result.zigzagLevelOrder(root)
    print(ans)
