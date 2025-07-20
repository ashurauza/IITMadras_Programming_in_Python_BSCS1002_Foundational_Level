def linear(P, Q, k):
    """
    A recursive function to determine if list P is a scalar multiple of list Q.

    Arguments:
    P -- list of integers
    Q -- list of integers
    k -- integer scalar

    Return:
    result -- bool (True if P == k * Q element-wise)
    """
    if len(P) != len(Q):
        return False  # Lists must be of the same length

    if len(P) == 0:
        return True  # Both lists are empty, hence scalar multiples

    if P[0] != k * Q[0]:
        return False  # If any element doesn't match, return False

    # Recursively check the rest of the lists
    return linear(P[1:], Q[1:], k)
