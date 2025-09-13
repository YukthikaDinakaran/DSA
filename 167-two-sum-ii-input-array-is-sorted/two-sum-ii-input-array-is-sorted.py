class Solution(object):
    def twoSum(self, numbers, target):
        n = len(numbers)
        left =0
        right = n-1
        sum = 0
        while left < right :
            sum = numbers[left]+numbers[right]
            if(sum == target):
                return [left+1, right+1]
            elif(sum < target):
                left = left+1
            else:
                right = right-1 

        
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        