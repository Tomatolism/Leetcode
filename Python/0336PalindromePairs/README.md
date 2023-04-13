注意事項
- iterate 不同string的長度時，要注意用len定義得到的數值，和for loop 中range的數值的差異。
- 根據參考解法。要記得先處理短的string片段。因此要先sort string list by len。
- 根據leetcode其他人的解答。
   -  更快的解法是，一開始的dictionary就是儲存reverse的string。在string分段iterate時，去找dictionary是否有所需要的字串。
   -  並且把含空string""的狀況分開處理
   -  這好處使只要一個dictionary。並且不用set儲存每步的結果。
   -  並且不需要sort



## 參考解法

https://www.youtube.com/watch?v=L7MmngL-iaM
