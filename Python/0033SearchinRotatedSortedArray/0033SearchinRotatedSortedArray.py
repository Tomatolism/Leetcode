class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1

        while l<=r:
            mid = (l+r) //2

            if nums[mid] == target : return mid
            if nums[l] == target : return l
            if nums[r] == target : return r


            if nums[mid] < nums[l]:
                if target > nums[mid] and target < nums[r]:
                    l = mid + 1
                    r -=1
                else:
                    l +=1
                    r = mid - 1
            elif nums[mid] > nums[r]:
                if target < nums[mid] and target > nums[l]:
                    l +=1
                    r = mid - 1 
                else:
                    l = mid + 1
                    r -=1
            else:
                if target < nums[mid]:
                    l +=1
                    r = mid -1
                else:
                    l = mid + 1
                    r -=1

        return -1            
