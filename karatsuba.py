
def karatsubas(x, y) -> int:
    """Multiply two integers together using Karatsuba's divide and conquer algorithm"""

    # Handle the base case
    if x < 10 or y < 10:
        return x * y
    
    # Calculate the base by the size of the numbers
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    # Split the numbers
    base = 10 ** m # calculate a base
    a, b = x // base, x % base
    c, d = y // base, y % base

    z1 = karatsubas(a, c)
    z2 = karatsubas(b, d)
    z3 = karatsubas(a+b, c+d)

    return z1 * base**2 + (z3 - z2 - z1)*base + z2

def main():
    # test the karatsuba function
    x = 123
    y = 21
    result = karatsubas(x, y)
    print(f"{x} * {y} = {result}")
    # test the karatsuba function
    assert karatsubas(123, 987) == 123*987

if __name__ == "__main__":
    main()
