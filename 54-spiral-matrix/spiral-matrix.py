class Solution(object):
    def spiralOrder(self, matrix):
        res = []
        left = 0
        right = len(matrix[0])-1
        top = 0
        bottom = len(matrix)-1
        while top <= bottom and left <= right:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top +=1
            for j in range(top, bottom+1):
                res.append(matrix[j][right])
            right -=1
            if top <= bottom :
                for i in range(right, left-1,-1 ):
                    res.append(matrix[bottom][i])
                bottom -=1 
            if left <= right:
                for j in range(bottom, top-1, -1):
                    res.append(matrix[j][left])
                left +=1
        return res



        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        