import pytest
from src.main import add

# --- 型チェックのテスト ---
@pytest.mark.parametrize("a,b,c,expected", [
    (1, 2, 3, 6),            # 正常ケース
    (1.5, 2.5, 3.0, 7.0),    # 小数もOK
    ("1", 2, 3, -1),         # aが非数値型
    (1, "2", 3, -1),         # bが非数値型
    (1, 2, "3", -1),         # cが非数値型
    (None, 2, 3, -1),        # Noneは非数値型
    ("x", "y", "z", -1),     # 全て非数値型
])
def test_type_check(a, b, c, expected):
    assert add(a, b, c) == expected


# --- 境界値チェックのテスト ---
@pytest.mark.parametrize("a,b,c,expected", [
    (0, 0, 0, 0),            # 下限境界
    (10, 10, 10, 30),        # 上限境界
    (-1, 5, 5, -2),          # aが範囲外
    (5, 11, 5, -2),          # bが範囲外
    (5, 5, 12, -2),          # cが範囲外
])
def test_boundary_check(a, b, c, expected):
    assert add(a, b, c) == expected


# --- 型と境界の複合テスト ---
@pytest.mark.parametrize("a,b,c,expected", [
    ("1", 5, 5, -1),         # 型エラー優先
    (11, "2", 3, -1),        # 型エラー優先
    (11, 2, 3, -2),          # 型OKだが範囲外
])
def test_combined_check(a, b, c, expected):
    assert add(a, b, c) == expected


# --- オプション引数なしのテスト ---
def test_default_c():
    assert add(3, 4) == 7
    assert add(10, 0) == 10
    assert add(11, 0) == -2
