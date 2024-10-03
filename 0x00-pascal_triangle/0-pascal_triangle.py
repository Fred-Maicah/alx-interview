#!/usr/bin/python3
"""
0pascal_triangle

"""
def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to n rows.
    Returns a list of lists of integers.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]  # First row is always [1]
    
    for i in range(1, n):
        row = [1]  # Each row starts with 1
        prev_row = triangle[i - 1]
        
        # Generate the interior elements of the row
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        
        row.append(1)  # Each row ends with 1
        triangle.append(row)
    
    return triangle
