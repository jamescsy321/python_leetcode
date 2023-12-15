from typing import List


# 57. Insert Interval
class Solution(object):
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # 當newInterval end < intervals start ，代表沒有重疊，newInterval在前，放入res
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # 當newInterval start > intervals end，代表沒有重疊，intervals較小，放入res
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                # 重疊處理比大小
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)

        return res


if __name__ == '__main__':
    result = Solution()
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    ans = result.insert(intervals, newInterval)
    print(ans)
