是使用union find的技巧。

union find有兩個部分。

第一個是find部分：用遞回的方式定義function，然後設定規則排序規則確保每個一個元件讀取時(規則定義在union的部分)，都會指向root的數值。
即使之後有指向的元件又再指向另一個新的元件時（ex: b > a, 但之後回圈讓a >c），因為遞迴設定的關係，讀取find(b)時，會連結到a再連結到c，這樣就能從而更新b的指向關係，使b > c

第二個是union。當兩個元件合併時，使用find找出兩個元件的root。設定排序規則（ex：Neetcode是另外定義rank參數; Guan是用string的大小關係），把其中一個元件的root取代成新的。


