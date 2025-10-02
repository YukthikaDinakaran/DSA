class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        
        # Step 1: Reverse top to bottom
        matrix.reverse()
        
        # Step 2: Transpose
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        