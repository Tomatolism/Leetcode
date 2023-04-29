使用dfs。

dfs傳遞的是node

如果是沒訪問過的node就創建新的node，並且依據original的node創建連結，透過dfs的function來連結新的node。

如果是已經訪問過的node，就回傳已創建好maping node的本身。讓前一層回圈的dfs建立連結。
