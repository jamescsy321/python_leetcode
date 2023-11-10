def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    reversed_num = 0
    temp = x

    while temp != 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp //= 10

    return reversed_num == x


def isPalindrome2(self, x: int) -> bool:
    if x < 0:
        return False
    # str(x)[::-1]：這部分將字串 str(x) 使用切片（slice）操作 [::-1] 進行反轉。這意味著它將返回原字串的倒序版本。
    # 例如，如果 str(x) 是"10"，則 str(x)[::-1] 將得到字串"01"。
    return str(x) == str(x)[::-1]


if __name__ == '__main__':
    num = 121
    result = isPalindrome(121)
    print(result)
