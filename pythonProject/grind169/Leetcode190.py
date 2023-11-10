# 190. Reverse Bits

def reverseBits(n: int) -> int:
    # 初始化
    ans = 0
    # 遍歷32位二進制所有內容
    for i in range(32):
        # 將ans左移一位，並取得n的最後一位數值
        ans = (ans << 1) + (n & 1)
        # 將數字右移一位
        n >>= 1
    #     回傳反轉後結果
    return ans


if __name__ == '__main__':
    n = 0b00000010100101000001111010011100
    result = reverseBits(n)
    print(result)
