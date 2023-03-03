"""
Reason of No AC in 1st submit:
Forget to sort list first

"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        
        for i, interval in enumerate(intervals):
            
            if i ==0:
                hold_interval = interval
            else:
                # If 2 interval do not overlap
                if hold_interval[1] < interval[0] or hold_interval[0] >interval[1]:
                    result.append(hold_interval)
                    hold_interval = interval
                else:
                    hold_interval[0] = min(hold_interval[0], interval[0])
                    hold_interval[1] = max(hold_interval[1], interval[1])

        result.append(hold_interval)
        return result
