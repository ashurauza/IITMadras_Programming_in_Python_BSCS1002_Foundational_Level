def ancestry(P, present, past):
    """
    A recursive function to compute the sequence of ancestors of a person.

    Arguments:
    P       -- dict: keys and values are strings; key is a person, value is their parent
    present -- str: current person
    past    -- str: the ancestor we are looking for

    Return:
    list of strings: sequence from 'present' to 'past' (inclusive), or empty if no such path
    """
    # Base case: if current person is the past person
    if present == past:
        return [present]

    # If person has no known parent
    if present not in P:
        return []

    # Recursive case: find parent and continue
    parent = P[present]
    ancestor_path = ancestry(P, parent, past)

    if ancestor_path:
        return [present] + ancestor_path  # Prepend current person to path

    return []  # No path found
