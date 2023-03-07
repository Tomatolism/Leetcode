"""
Set two pointer at two end of array.
Moving the pointer which have smaller value
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start_index = 0
        end_index = len(height)-1
        max_area = 0

        while start_index<end_index:
            start_height = height[start_index]
            end_height = height[end_index]

            length = end_index - start_index

            area = length * min(start_height, end_height)
            max_area = max(max_area, area)

            if start_height < end_height:
                start_index += 1
            else:
                end_index -= 1

        return max_area
