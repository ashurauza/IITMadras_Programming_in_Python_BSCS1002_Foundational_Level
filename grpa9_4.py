def steps(n):
    """
    A recursive function to compute the number of ways to ascend steps,
    taking 1, 2, or 3 steps at a time.

    Argument:
    n -- integer

    Return:
    result -- integer (number of ways to reach the nth step)
    """
    # Base cases
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    # Recursive case
    return steps(n - 1) + steps(n - 2) + steps(n - 3)
