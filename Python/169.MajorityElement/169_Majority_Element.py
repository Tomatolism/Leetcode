class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        total_n = len(nums)
        hash_table = {}
        for value in nums:
            if value in hash_table:
                hash_table[value] +=1
                if hash_table[value] > total_n/2:
                    return value
            else:
                hash_table[value] = 1
        return max(hash_table, key=hash_table.get)
        
