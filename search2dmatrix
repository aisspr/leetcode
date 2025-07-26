def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    """
    You are given an m x n integer matrix matrix with the following two properties:
    
    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.
    Given an integer target, return true if target is in matrix or false otherwise.
    
    You must write a solution in O(log(m * n)) time complexity.
    """
    rows, cols = len(matrix), len(matrix[0])
    total_el = rows*cols
    low, high = 0, total_el - 1

    while low <= high:
        mid = low + (high - low) // 2
        mid_row = mid //2
        mid_col = mid % 2

        current_val = matrix[mid_row][mid_col]

        if current_val == target:
            return True
        elif current_val < target:
            low = mid + 1
        else:
            high = mid -1
    return False
