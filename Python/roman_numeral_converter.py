"""
roman_numeral_converter.py
Convert integers (1..3999) to Roman numerals.

Usage:
    python3 roman_numeral_converter.py 1994
    # => MCMXCIV
"""

def to_roman(n: int) -> str:
    if not (1 <= n <= 3999):
        raise ValueError("Input must be between 1 and 3999")

    pairs = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I"),
    ]

    res = []
    for val, sym in pairs:
        count, n = divmod(n, val)
        res.append(sym * count)
        if n == 0:
            break
    return "".join(res)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 roman_numeral_converter.py <number 1..3999>")
        sys.exit(1)
    print(to_roman(int(sys.argv[1])))
