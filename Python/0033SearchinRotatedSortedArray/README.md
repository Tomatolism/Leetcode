本題是binary search的變形。

因為每個element都是unique的遞增數列，經過rotate後，左側的boundary必定大於右側的boundary（除非是未經rotate的嚴格遞增數列）

基本上有三種情況。
1. mid point座落在rotating Pivot的左邊 ： 
   > 特性: mid point的數值大於 左方的boundary （同時小於右方的boundary）
3. mid point座落在rotating Pivot的右邊 ：
   > 特性: mid point的數值小於 右方的boundary （同時大於左方的boundary）
5. 成為非rotating的數列

根據三種情況下，分別找出對應的條件是，當找出的數值不等於mid point時，是要將l還是r的boundary 移動到mid point。

第一種版本是偷懶，不思考結果剛好落在boundary的情況。每次都確認boundary和mid是否符合target。缺點是比較慢，程式碼比較長

第二種版本考量過結果落在boundary的情況。

