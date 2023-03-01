class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # define pointer 
        i, j = 0, 1

        n_len = len(prices)
        max_profit = 0
        
       
        while j<n_len:
            value_i = prices[i]
            value_j = prices[j]
            if value_j > value_i:
                profit = value_j - value_i
                
                # save the max profit
                max_profit = max(profit, max_profit)
                j += 1

            else:
              # if the value at index j in smaller than the value at index i, then set i to the new index
                i, j = j, j+1

        return max_profit
      
      
      
"""
Miss case:
1. When interval == []
2. When Newinterval is large than all in interval 
"""
