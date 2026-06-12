def add(a, b, c=0, *, min_value=None, max_value=None):
    # --- 型チェック ---
    for name, value in {"a": a, "b": b, "c": c}.items():
        if not isinstance(value, (int, float)):
            return f"type error: {name} must be int or float"

    # --- 計算 ---
    result = a + b + c

    # --- 境界値チェック ---
    if min_value is not None and result < min_value:
        return f"boundary error: result {result} < min_value {min_value}"

    if max_value is not None and result > max_value:
        return f"boundary error: result {result} > max_value {max_value}"

    return result
