def add(a, b, c=0):
    # 型チェック
    for value in (a, b, c):
        if not isinstance(value, (int, float)):
            return -1

    # 境界値チェック
    if not (0 <= a <= 10 and 0 <= b <= 10 and 0 <= c <= 10):
        return -2

    # 正常処理
    return a + b + c
