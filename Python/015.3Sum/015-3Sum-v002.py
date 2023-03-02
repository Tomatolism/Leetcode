class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for a in range(len(nums)):
            if a > 0 and nums[a] == nums[a-1]:
                continue

            left = a + 1
            right = len(nums) -1
            target = -nums[a]

            while left < right:
                if nums[left] + nums[right] == target:
                    result.append([nums[a], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # ingore repeated value
                    ## left < right is not neccesary here, 
                    ## just to break while loop if there is all repeat value 

                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                    while left < right and nums[right] == nums[right+1]:
                        right -=1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left +=1

        return result
