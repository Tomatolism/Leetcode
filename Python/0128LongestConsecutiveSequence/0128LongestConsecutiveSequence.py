class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest = 0

        for value in nums_set: ## loop through the set of nums is much faster than nums
            if value - 1 not in nums_set:
                length = 0
                while value in nums_set:
                    length +=1
                    longest = max(longest, length)
                    value +=1

        return longest
