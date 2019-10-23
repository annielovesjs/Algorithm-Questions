class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_length=0
        table = {0: 0}
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            
            if count in table:
                max_length = max(max_length, i + 1 - table[count])
            else:
                table[count] = i + 1
        
        return max_length
 