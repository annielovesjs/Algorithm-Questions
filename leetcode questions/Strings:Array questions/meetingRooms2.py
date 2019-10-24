class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        #sort based on end and start times 
        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals)
        e = 0
        result = 0
        
        for i in range(len(intervals)):
            if start[i] < end[e]:
                result+=1
            else:
                e+=1
                
        return result