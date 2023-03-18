
方法一：
將所有interval排序，
loop所有的interval。
偵測Loop的interval和前一個interval是否有重疊。
如果有重疊
  > 保留結束時間最早的（更新新的結束時間）
  > 拋棄結束時間晚 （拋棄數）
如果沒有重疊
  > 更新新的結束時間

# Reference
[NeetCode: Non-Overlapping Intervals - Leetcode 435 - Python](https://www.youtube.com/watch?v=nONCGxWoUfM)
    
    
