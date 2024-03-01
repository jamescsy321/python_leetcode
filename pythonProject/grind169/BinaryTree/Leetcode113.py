from typing import Optional, List


# 113. Path Sum II
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def find_path(curr_node, target_sum, curr_path, all_paths):
            if not curr_node:
                return
            curr_path.append(curr_node.val)

            if curr_node.val == target_sum and not curr_node.left and not curr_node.right:
                all_paths.append(list(curr_path))
            else:
                target_sum -= curr_node.val
                find_path(curr_node.left, target_sum, curr_path, all_paths)
                find_path(curr_node.right, target_sum, curr_path, all_paths)
            curr_path.pop()

        all_paths = []
        find_path(root, targetSum, [], all_paths)
        return all_paths


if __name__ == '__main__':
    result = Solution()
    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                    TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
    targetSum = 22
    ans = result.pathSum(root, targetSum)
    print(ans)
