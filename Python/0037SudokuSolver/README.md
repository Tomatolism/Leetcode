## coding反省
- 第一次寫DFS還要再複習
- 9x9方塊的部分，正確的定義為square_i, square_j = i//3*3, j//3*3 
- 執行dfs(0,0)就會自動in-place修改board的內容。
- 因為是唯一解，因此會持續in place修改board內容。直到正確為止
- index的細節設定要注意


## 「深度優先搜索」說明 by ChatGPT

深度優先搜索（Depth-First Search，簡稱DFS）是一種用於搜尋或遍歷圖或樹等數據結構的演算法。DFS 的基本思想是從一個起始節點開始，不斷選擇一個相鄰節點進行遍歷，直到達到最深的節點，然後再回溯（回退）到上一個節點，並繼續遍歷未被訪問的節點，直到所有節點都被訪問。

常見的 DFS 程式架構如下：

```
1. 創建一個遞迴函數，傳入當前節點作為參數。
2. 在遞迴函數中，先標記當前節點為已訪問，並執行當前節點的相應操作。
3. 遍歷當前節點的所有相鄰節點，如果相鄰節點未被訪問，則遞迴調用該節點為新的當前節點。
4. 若所有相鄰節點都已被訪問，則回溯到上一個節點，繼續遍歷未被訪問的節點。
5. 當所有節點都被訪問完畢，遍歷結束。
```

DFS 的程式架構通常使用遞迴方式實現，因為 DFS 的過程天然具有遞迴的性質，可以使用遞迴深度來記錄節點的訪問順序，並方便地回溯到上一個節點。此外，也可以使用類似堆疊（Stack）的資料結構來模擬遞迴過程，實現非遞迴的 DFS。在選擇相鄰節點時，DFS 沒有固定的選擇策略，可以根據具體應用場景進行調整，例如選擇第一個相鄰節點、最後一個相鄰節點、或者根據某種權重來選擇相鄰節點等。


下面為一個python 範例

```python
# 定義圖的節點類別
class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
        self.visited = False

# 深度優先搜索函數
def dfs(node):
    # 標記當前節點為已訪問
    node.visited = True
    print("訪問節點：", node.val)
    
    # 遍歷當前節點的相鄰節點
    for neighbor in node.neighbors:
        # 如果相鄰節點未被訪問，則遞迴調用 dfs 函數
        if not neighbor.visited:
            dfs(neighbor)

# 創建一個簡單的圖
#    1
#  /   \
# 2     3
#      / \
#     4   5
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# 建立節點之間的相鄰關係
node1.neighbors = [node2, node3]
node3.neighbors = [node4, node5]

# 從節點1開始進行深度優先搜索
dfs(node1)
```
