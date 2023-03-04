class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        point_index = 0 
        start = 0
        end = len(nums) - 1

        while point_index<= end:
            if nums[point_index] == 0:
                nums[point_index], nums[start] = nums[start], nums[point_index]
                point_index +=1
                start += 1
            elif nums[point_index] ==1:
                point_index +=1
            else:
                nums[point_index], nums[end] = nums[end], nums[point_index]
                end -=1

