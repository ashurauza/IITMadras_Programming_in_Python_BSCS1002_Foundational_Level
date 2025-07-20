'''Given a square matrix M and two indices (i,j), M ij is the matrix obtained by removing the i th row and the j th column of M.

Write a function named minor_matrix that accepts three arguments:

M: a square matrix
i: a non-negative integer
j: a non-negative integer
The function should return the matrix M ij after removing the i th row and the j th column of M. Note that we use zero-based indexing throughout. That is, if the 
matrix M is of dimensions n×n, then we have 0≤i,j≤n−1.

(1) You can assume that the number of rows in M will be at least 3 in each test case.
(2) You do not have to accept input from the user or print the output to the console.'''
def minor_matrix(M, i, j):
    """
    Compute the "minor matrix"

    Arguments:
        M: list of lists
        i: integer
        j: integer
    Return:
        M_ij: list of lists
    """
    # Exclude the i-th row and j-th column
    return [row[:j] + row[j+1:] for k, row in enumerate(M) if k != i]




#OR

 
#def minor_matrix(M, i, j):
    """
    Compute the minor matrix Mij by removing the ith row and jth column.
    
    Arguments:
    M -- list of lists, representing a square matrix
    i -- integer, index of the row to remove
    j -- integer, index of the column to remove
    
    Returns:
    A new matrix (list of lists) with the ith row and jth column removed
    """
    # result = []

    # for row_index in range(len(M)):
    #     if row_index == i:
    #         continue  # Skip the ith row
    #     new_row = []
    #     for col_index in range(len(M[0])):
    #         if col_index == j:
    #             continue  # Skip the jth column
    #         new_row.append(M[row_index][col_index])
    #     result.append(new_row)
    
    # return result
