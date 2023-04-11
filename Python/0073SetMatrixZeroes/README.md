### space complexity分析
- 方法1  O(m x n)：設立同等大小矩陣，用來標記0的位置。
- 方法2  O(m + n): 分別製作row 和col的array來標記出現0的位置。
- 方法3  O(1):直接使用matrix最邊緣的儲存格，來標記各行列是否出現0。

使用方法3時，最左上角的部分，因為會row和col會重複使用到，因此另外設計一個parameter來標記第一排col matrix[i][0]的結果。

### 演算流程：
1. scan所有儲存格，label所有0的位置
2. 將第二排起始的row和col根據標記的結果改為0
3. 若最左上角為0，將第一排col依據結果改為0
4. 根據額外的paremeter，若為true，將第一排row改為0

### 參考資料

Neetcode
