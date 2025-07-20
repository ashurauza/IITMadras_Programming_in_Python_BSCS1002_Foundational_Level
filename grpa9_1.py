def reverse(L):
    """
    A recursive function to reverse a list L

    Arguments:
    L -- list (type of elements can be anything)

    Return:
    result -- list reversed
    """
    if len(L) == 0:
        return []  # Base case: empty list
    else:
        return [L[-1]] + reverse(L[:-1])  # Recursive case
