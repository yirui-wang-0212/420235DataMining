# bii

## 1 代码运行结果拷贝

结果见`bii/Output`目录下文件

![image-20180506215114402](/var/folders/k0/973jdnld69s9y260lpyk5xww0000gn/T/abnerworks.Typora/image-20180506215114402.png)

![image-20180506215129272](/var/folders/k0/973jdnld69s9y260lpyk5xww0000gn/T/abnerworks.Typora/image-20180506215129272.png)

## 2 讨论分析

`关于pattern数`

`trade.csv	`

| Support | 2      | 4    | 6    | 8    | 10   | 12   |
| ------- | ------ | ---- | ---- | ---- | ---- | ---- |
| dptno   | 38770  | 946  | 317  | 155  | 94   | 68   |
| pluno   | 946407 | 8071 | 1919 | 815  | 466  | 287  |
| bndno   | 1000   | 153  | 76   | 40   | 23   | 17   |

`trade_new.csv`

| Support | 2       | 4     | 6    | 8    | 10   | 12   |
| ------- | ------- | ----- | ---- | ---- | ---- | ---- |
| dptno   | 40440   | 2331  | 837  | 459  | 288  | 196  |
| pluno   | 1150867 | 21914 | 6497 | 3093 | 1771 | 1138 |
| bndno   | 9462    | 846   | 340  | 194  | 120  | 101  |

- `pattern数`随着 `support`增大而减小，由于`support`表示支持度，支持度越低，符合的`pattern数`越多
- 相对于`bi`各个`support`对应的`pattern数`都变大了，由于将一个用户的多个订单组合，则各个`item`之间的组合次数也增多了
- 一个用户的所有`transaction`具有先后顺序，故具有`sequence`形式，一个内没有时间先后顺序，与`aii`结果不相同

## 3 性能比较

![5ECE3036D6C1E993E9B689D017A5A4AA](/Users/yigritte/Desktop/5ECE3036D6C1E993E9B689D017A5A4AA.png)