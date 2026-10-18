def factorial_loop(n):
    """Return n! using an iterative loop."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    """Return n! using recursion."""
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    raw = input("Enter a non-negative integer: ").strip()
    try:
        number = int(raw)
    except ValueError:
        print("Please enter a valid integer.")
    else:
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"{number}! (loop) = {factorial_loop(number)}")
            print(f"{number}! (recursion) = {factorial_recursive(number)}")
