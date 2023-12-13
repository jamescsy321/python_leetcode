import heapq
from typing import List

# 973. K Closest Points to Origin
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x):
            return x[0] ** 2 + x[1] ** 2

        points.sort(key=dist)
        return points[:k]

    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        # 在線性時間內將 list x 轉為 heap
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            # 從 heap 取出並回傳最小的元素
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res

    def kClosest3(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            # heapq 模組實現的是最小堆（min heap）。在堆中，最小的元素位於頂部，但我們希望最大值在頂部，因此將元素值平方後取負數可達成
            # 在最小堆中將最大值至於頂部作用
            dist = -(x * x + y * y)
            # 當堆的大小與K值相同，將新的點推進堆中並且取出頂部元素，這樣就可維持K個
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))

        return [(x, y) for (dist, x, y) in heap]


if __name__ == '__main__':
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    result = Solution()
    ans = result.kClosest3(points, k)
    print(ans)
