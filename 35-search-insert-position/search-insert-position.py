class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        if n == 0:
            return 0
        if n==1:
            if target <= nums[n-1]:
                return 0
            else:
                return 1
        if target<=nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        if target == nums[-1]:
            return len(nums) -1 
        left,right = 0, n-1
        while left <=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
        
