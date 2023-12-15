from functools import reduce

# 844. Backspace String Compare
# stack

class Solution:
    def backspcaeCompare(self, s: str, t: str) -> bool:
        def back(res, c):
            if c != '#':
                res.append(c)
            elif res:
                res.pop()
            return res

        # s_result = reduce(back, s, [])

        return reduce(back, s, []) == reduce(back, t, [])

    # two pointer method
    def backspcaeCompare2(self, s: str, t: str) -> bool:
        # 確認井符號
        def sign_check(strings, idx):
            skip = 0
            while idx >= 0:
                if strings[idx] == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    break
                idx -= 1
            return idx

        idx1 = len(s) - 1
        idx2 = len(s) - 1

        while idx1 >= 0 or idx2 >= 0:
            i1 = sign_check(s, idx1)
            i2 = sign_check(t, idx2)

            if i1 < 0 and i2 < 0:
                return True
            if i1 < 0 or i2 < 0:
                return False
            if s[i1] != t[i2]:
                return False

            idx1 = i1 - 1
            idx2 = i2 - 1
        return True


if __name__ == '__main__':
    solution = Solution()
    result = solution.backspcaeCompare("ab#c", "ad#c")
    print("result=", result)
