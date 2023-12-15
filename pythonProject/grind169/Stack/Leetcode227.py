# 227. Basic Calculator II
class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        curr_num = 0
        operator = "+"
        operators = {"+", "-", "*", "/"}
        nums = set(str(x) for x in range(10))

        for idx, char in enumerate(s):
            if char in nums:
                '''
                curr_num * 10 + (ord(char) - ord("0"))：這個運算式將先前已構建的數字乘以10（相當於將其左移一位），
                然後加上目前處理的數字字符所對應的數字值，從而將其添加到目前正在構建的數字後面。這樣可以將連續的數字字符組合成完整的數字
                ，例如從 "123" 中構建出整數 123。
                '''
                curr_num = curr_num * 10 + (ord(char) - ord("0"))
            #     如果目前處理的字符是運算符號，或者已經處理到了字串的最後一個字符，則進行後續的運算處理。
            if char in operators or idx == len(s) - 1:
                if operator == "+":
                    stack.append(curr_num)
                elif operator == "-":
                    stack.append(-curr_num)
                elif operator == "*":
                    temp_num = stack.pop()
                    stack.append(temp_num * curr_num)
                else:
                    temp_num = stack.pop()
                    stack.append(int(temp_num / curr_num))

                curr_num = 0
                operator = char

        return sum(stack)


if __name__ == '__main__':
    result = Solution()
    s = "3+2*2"
    ans = result.calculate(s)
    print(ans)
