class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        n = len(intervals)

        if n<=1:
            return True
            
        for i in range(1, n):
            pre_interval = intervals[i-1]
            cur_interval = intervals[i]

            if pre_interval[1] > cur_interval[0]:
                return False
            
        return True
