class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #keep track of element at the start and the end ->
        #keep track of the middle -1 and middle + 1
        #if middle + 1 bigger than middle, start -> middle
        #if middle + 1 smaller than middle && middle -1 bigger-> end = middle
        #else if middle - 1 < middle and middle + 1 > middle -> return middle
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        start = 0
        end = len(nums) - 1
        
        while start < end:
            middle = int((start + end) / 2)
            if nums[middle+1] > nums[middle]:
                start = middle + 1 
            else:
                if nums[middle-1] < nums[middle]:
                    return middle
                else:
                    end = middle - 1
        return end
        
                    