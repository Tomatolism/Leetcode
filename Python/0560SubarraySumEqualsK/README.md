

# 方法一：Prefix-sum（cumulate）
使用Hash table儲存所有的Prefix-sum的結果
然後抓新的Prefix-sum和target的difference，
如果difference有出現在Hash table，
表示從difference的結尾到現在的Prefix-sum的位置之間的subarray之和，
是滿足target的subarray



參考資料
Subarray Sum Equals K - LeetCode 560 - Coding Interview Questions(後半為Prefix)
https://www.youtube.com/watch?v=EFzYA9H0MfQ
