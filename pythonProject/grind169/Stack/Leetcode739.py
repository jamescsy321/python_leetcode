from typing import List


# 739. Daily Temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 初始化一個stack並將長度設為temperatures的長度並將值都初始為0
        ans = [0] * len(temperatures)
        # 初始一個stack之後要放入index
        stack = []
        '''
        enumerate取得index及數值，temperatures[stack[-1]]為取得temperatures top 數值
        迴圈後將index及數值取得，如果stack有值且temperature[stack的最上層的值]大於目前溫度
        將stack最上層的值取出並用目前index-cur所代表的之前的index帶入ans[cur]
        '''
        for i, cur_temp in enumerate(temperatures):
            if stack and temperatures[stack[-1]]:
                cur_temp = temperatures[stack[-1]]
            while stack and temperatures[stack[-1]] < cur_temp:
                last_index = stack.pop()
                ans[last_index] = i - last_index
            stack.append(i)

        return ans


if __name__ == '__main__':
    result = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    answer = result.dailyTemperatures(temperatures)
    print(answer)
