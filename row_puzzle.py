# Author: Ashlyn Musgrave
# GitHub Username: ashlyn-musgrave
# Date: 7/26/2023
# Description: This program takes a list of integers (the row) as a parameter and returns True
# if the puzzle is solvable (getting the token to the rightmost square) for that row, but returns False otherwise.

def row_puzzle(row, pos=0):
    """This function returns True if the puzzle is solvable and gets the token to the
     rightmost square for that row, but returns False otherwise."""

    #First we define the base case that we want to compare against
    if row[pos] == 0:
        return True

    else:
        left = pos - row[pos]
        right = pos + row[pos]

        if left >= 0 and row[left] != None:
            if row_puzzle(row, left):
                return True
        if right < len(row) and row[right] != None:
            if row_puzzle(row, right):
                return True

        return False