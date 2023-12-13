from typing import List

# 252 Meeting Rooms
# Array

'''
Given an array of meeting time intervals where intervals[i] = [start,end]
,determine if a person could attend all meetings

Example 1:
Input:
intervals = [[0,30],[5,10],[15,20]]
output:false
Example 2:
Input:
intervals = [[7,10],[2,4]]
output:true
'''


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # 將陣列排序
        intervals.sort()
        i = 1

        while i < len(intervals):
            # 比較前面的end跟後面的start大小，如果前面的比較大就代表衝突
            if intervals[i][0] < intervals[i - 1][1]:
                return False
            i += 1

        return True


if __name__ == '__main__':
    intervals = [[0, 30], [5, 10], [15, 20]]
    result = Solution()
    ans = result.canAttendMeetings(intervals)
    print(ans)
