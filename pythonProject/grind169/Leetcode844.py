from functools import reduce


class Solution:
    def backspcaeCompare(self, s: str, t: str) -> bool:
        def back(res, c):
            if c != '#':
                res.append(c)
            elif res:
                res.pop()
            return res

        s_result = reduce(back, s, [])

        return reduce(back, s, []) == reduce(back, t, [])


if __name__ == '__main__':
    solution = Solution()
    result = solution.backspcaeCompare("a#c", "b")
    print("result=", result)
