def hammingWeight(n: int)-> int:
    ans = 0
    while n:
        n &= (n - 1)
        ans += 1
    return ans

# if __name__ == '__main__':
#     result = hammingWeight(111)
#     print(result)