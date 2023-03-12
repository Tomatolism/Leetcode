class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        count = 0 
        hash_table = {0:1}
        for value in nums:
            pre_sum += value

            if pre_sum - k in hash_table:
                count += hash_table[pre_sum - k]

            if pre_sum in hash_table:
                hash_table[pre_sum] +=1
            else:
                hash_table[pre_sum] = 1

        return count
