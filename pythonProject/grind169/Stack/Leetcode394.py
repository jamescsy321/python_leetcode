# 394. Decode String
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = []
        curr_num = 0

        for char in s:
            if char == "[":
                stack.append(curr_str)
                stack.append(curr_num)
                curr_str = []
                curr_num = 0
            elif char == "]":
                num = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + curr_str * num
            elif char.isdigit():
                curr_num = curr_num * 10 + int(char)
            else:
                curr_str.append(char)

        return "".join(curr_str)


if __name__ == '__main__':
    result = Solution()
    s = "3[a2[c]]"
    ans = result.decodeString(s)
    print(ans)
