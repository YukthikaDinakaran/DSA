class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        arr = [(num, i) for i, num in enumerate(nums)]
        arr.sort()
        left = 0
        right = n -1
        while(left < right):
            if arr[left][0]+ arr[right][0] == target:
                return [arr[left][1], arr[right][1]]
            elif arr[left][0]+ arr[right][0] < target:
                left = left+1
            else:
                right = right-1