- 第一版本是用先看在哪個row，確定row的位置後，確認在col。
- 因此要考慮數值比全部大或小。避免matrix[row][col]超出範圍。 return error

- official solution更快。直接用 left, right = 0, m*n -1。
- 定義為： matrix[pivot_idx // n][pivot_idx % n]
