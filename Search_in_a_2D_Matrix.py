class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Check if the matrix is None or empty. If so, return False immediately.
        if matrix == None or len(matrix) == 0:
            return False

        # Determine the number of rows (m) and columns (n) in the matrix.
        m = len(matrix)  # Number of rows
        n = len(matrix[0])  # Number of columns

        # Define the search space using a 1D index range [0, m*n - 1].
        start = 0  # Start index of the search space
        end = m * n - 1  # End index of the search space

        # Perform binary search on the virtual 1D representation of the matrix.
        while start <= end:
            # Find the middle index of the current search space.
            mid = start + (end - start) // 2

            # Convert the 1D index (mid) back to 2D matrix indices (row and col).
            row = mid // n  # Row index
            col = mid % n  # Column index

            # Check if the element at the calculated position matches the target.
            if matrix[row][col] == target:
                return True  # Target found, return True.

            # If the current element is less than the target, narrow the search to the right half.
            elif matrix[row][col] < target:
                start = mid + 1  # Update the start index.

            # If the current element is greater than the target, narrow the search to the left half.
            else:
                end = mid - 1  # Update the end index.

        # If the loop completes without finding the target, return False.
        return False

# Time Complexity:
# O(log(m * n)) -> Since we perform binary search on a virtual 1D array of size m * n,
#                  where m is the number of rows and n is the number of columns.

# Space Complexity:
# O(1) -> Constant space is used as no additional data structures are used, 
#         and the computations are performed in-place.

            
        
