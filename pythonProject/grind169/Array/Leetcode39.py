from typing import List


# 39. Combination Sum
# recursive 方式處理
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []

        def backtracking_helper(candidates, temp_list, remainder, index):
            if remainder == 0:
                self.res.append(temp_list[:])
                return
            if remainder < 0:
                return

            for i in range(index, len(candidates)):
                temp_list.append(candidates[i])
                backtracking_helper(candidates, temp_list, remainder - candidates[i], i)
                temp_list.pop()

        backtracking_helper(candidates, [], target, 0)
        return self.res


if __name__ == '__main__':
    result = Solution()
    candidates = [2, 3, 5]
    target = 8
    ans = result.combinationSum(candidates, target)
    print(ans)
