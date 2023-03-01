class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        def check_overlap(List1, List2):
            """
            Check if 2 interval overlap

            Return:
                Boolean: True if 2 interval overlap, False otherwise
            """
            start1 ,end1 = List1[0], List1[1]
            start2 ,end2 = List2[0], List2[1]
            if start1 > end2 or start2 > end1:
                return False
            else: 
                return True

        result = []
        for i, each_intervals in enumerate(intervals):
            if check_overlap(each_intervals, newInterval):
                newInterval[0] = min(each_intervals[0], newInterval[0])
                newInterval[1] = max(each_intervals[1], newInterval[1])

            else:
                end_new = newInterval[1]
                start_each = each_intervals[0]
                if end_new < start_each  :
                    result.append(newInterval)
                    result += intervals[i:]
                    return result
                else:
                    result.append(each_intervals)

        result.append(newInterval)     
        return result                   





      
"""
Miss point:
1. When interval == []
2. When Newinterval is large than all in interval 
3. way to append list on a list
"""
