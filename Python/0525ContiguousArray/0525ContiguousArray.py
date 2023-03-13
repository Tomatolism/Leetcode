class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefixsum = 0
        hashTable = {0:0}
        max_length = 0 
        for i, value in enumerate(nums, start= 1):
            if value == 0:
                prefixsum +=1
            else:
                prefixsum -=1
            
            if prefixsum in hashTable:
                length = i - hashTable[prefixsum] 
                max_length = max(length, max_length)
            else:
                hashTable[prefixsum] = i

        return max_length
