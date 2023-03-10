class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalBalance = 0
        current_start_i = 0
        current_Balance = 0

        for i in range(len(gas)):
            balance = gas[i] - cost[i]
            totalBalance += balance
            current_Balance += balance

            if current_Balance <0:
                current_start_i = i+1
                current_Balance = 0
            
        if totalBalance < 0:
            return -1
        else:
            return current_start_i
