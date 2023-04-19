- constrain：中位數的位置必為兩個list的平均值。
- 兩者皆為嚴格遞增list
- 用這個constrain，可以只在比較短的list設定two pointer跟partition。讓長的list的partition跟著連動
- 比較上下partition左右。正確的時候，兩個list的partition左側兩個數值，都要小於右側。

注意點
- partition的設定時，會超過list的讀取空間。要用if和float('inf')或float('-inf')處理超出範圍的數值。
- 總數為偶數時，中位數要平均。總數為奇數時，根據partition的定義方式取一個值。
