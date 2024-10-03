def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]  # First row of Pascal's triangle is always [1]
    
    for i in range(1, n):
        row = [1]  # Each row starts with 1
        prev_row = triangle[i - 1]
        
        # Calculate the values in between the first and last element of the row
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        
        row.append(1)  # Each row ends with 1
        triangle.append(row)
    
    return triangle
