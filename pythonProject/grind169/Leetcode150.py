from typing import List


# 150. Evaluate Reverse Polish Notation
# 逆波蘭表示法，數字在前運算符在後
# 當碰到運算符時將前兩個數字取出並用所遇到運算符處理後在放入stack
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))

        return stack[0]


if __name__ == '__main__':
    result = Solution()

    tokens = ["2", "1", "+", "3", "*"]
    ans = result.evalRPN(tokens)
    print(ans)
