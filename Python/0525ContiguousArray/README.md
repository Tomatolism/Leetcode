使用Prefixsum的方式

array sum[i:j]= prefixsum[j] - prefixsum[i]

當要找subarray中有相同數量的0和1
表示Prefixsum值相同的兩點間，0,1的數量相同。
因此做法是，把Prefixsum第一次出現的某個數值的index用hashtable記錄起來，
隨後每算一個prefixsum就確認hashtable是否出現過，若出現就計算長度，並與目前為止的最大長度比較


參考資料
https://www.youtube.com/watch?v=uYuSLvjEyjQ
