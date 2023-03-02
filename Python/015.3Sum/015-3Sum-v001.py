class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result_list, dups = set(), set() 
        hash_map = {}

        for i in range(len(nums)):
            val1 = nums[i]
            if val1 not in dups:
                dups.add(val1)
                for j in range(i+1, len(nums)):
                    val2 = nums[j]
                    complement = -val1 - val2
                    if (complement in hash_map) and hash_map[complement] ==i:
                        result_list.add(tuple(sorted((val1, val2, complement))))
                        
                    hash_map[val2] = i

        return set(result_list)
