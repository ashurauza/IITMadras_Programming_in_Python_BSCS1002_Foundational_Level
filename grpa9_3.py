def collatz(n):
    """
    A recursive function to compute the number of calls to the Collatz function of n

    Argument:
    n -- integer (Assume that 1 < n <= 32000)

    Returns:
    result -- integer (number of recursive calls to reach 1)
    """
    if n == 1:
        return 0  # Base case: no more calls needed if n is 1

    if n % 2 == 0:
        return 1 + collatz(n // 2)  # If n is even: divide by 2
    else:
        return 1 + collatz(3 * n + 1)  # If n is odd: 3n + 1
