class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def sweep_list(target_list, start, end):
            while start < end:
                target_list[start], target_list[end] = target_list[end], target_list[start]
                start +=1
                end -=1
        k = k%len(nums)
        sweep_list(nums, start=0, end=len(nums)-1)
        sweep_list(nums, start=0, end=k-1)
        sweep_list(nums, start=k, end=len(nums)-1)
