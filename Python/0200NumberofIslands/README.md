嘗試使用python 定義邊界的方式 

```
i in range(rows)
```
取代
```
0 <= i <rows
```

但這樣速度慢很多。因為這個上方的運算time complexity是O(n)
下面的邏輯判斷是O(1)
修改回邏輯判斷後，速度從 20%提升到50%
