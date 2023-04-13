注意事項
- iterate 不同string的長度時，要注意用len定義得到的數值，和for loop 中range的數值的差異。
- 根據參考解法。要記得先處理短的string片段。因此要先sort string list by len。
- 用訪問過後，才存到set中，只核對set的片段，來避免出現一樣的結果。

- 根據leetcode其他人的解答。
   -  更快的解法是，一開始的dictionary就是儲存reverse的string。在string分段iterate時，去找dictionary是否有所需要的字串。
   -  這好處使只要一個dictionary。並且不用set儲存每步的結果。
   -  並且不需要sort
   -  為了避免回答重複的組合，在掃描string左右的l和r時候，l是不會出現""表示r永遠會少掉第一個字母，只有l會有完整的string。透過這樣確保兩個字串是彼此的reverse時，只有l會執行配對。r不會執行配對。
   -  因為上述設定，因此要把含空string""的狀況分開處理



## 參考解法

https://www.youtube.com/watch?v=L7MmngL-iaM
