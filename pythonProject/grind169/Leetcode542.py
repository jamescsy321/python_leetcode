from collections import deque
from typing import List

# 542. 01 Matrix
class Solution():
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        DIR = [0, 1, 0, -1, 0]
        q = deque([])
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1  # Marked as not processed yet!

        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if nr < 0 or nr == m or nc < 0 or nc == mat[nr][nc] != -1:
                    continue
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))
        return mat

    def updateMatrix2(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        # 創建一個集合 visit 來追蹤已訪問過的位置
        visit = set()
        # 創建一個雙端隊列 q 來實現廣度優先搜索
        q = deque()
        # 找出所有矩陣中值為 0 的位置，將這些位置加入 visit 集合中並加入隊列 q 中。
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    visit.add((r, c))
                    q.append((r, c))
        # while q:: 當隊列不為空時，持續進行以下操作：
        # 從隊列中取出一個位置 (r, c)。
        # 使用 for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]: 遍歷四個方向。
        # 對於每個方向，計算新的位置 (row, col)。
        # 如果新位置 (row, col) 在矩陣範圍內且未被訪問過，則更新該位置的值為當前位置 (r, c) 的值加一，表示到最近的零值位置的距離。
        # 將新位置 (row, col) 加入 visit 集合中並加入隊列 q 中，以便之後處理。
        # 最後返回更新後的矩陣 mat。
        while q:
            r, c = q.popleft()
            # 遍歷四個方向
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                row, col = r + dr, c + dc
                if 0 <= row < rows and 0 <= col < cols and (row, col) not in visit:
                    mat[row][col] = mat[r][c] + 1
                    visit.add((row, col))
                    q.append((row, col))

        return mat


if __name__ == '__main__':
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]

    result = Solution()
    ans = result.updateMatrix2(mat)
    print(ans)
