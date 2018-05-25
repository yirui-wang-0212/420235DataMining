# aii

## 1 代码运行结果拷贝

结果见``aii/Output``目录下文件

![image-20180506211007148](/var/folders/k0/973jdnld69s9y260lpyk5xww0000gn/T/abnerworks.Typora/image-20180506211007148.png)

![image-20180506211031735](/var/folders/k0/973jdnld69s9y260lpyk5xww0000gn/T/abnerworks.Typora/image-20180506211031735.png)

## 2 讨论分析

`关于pattern数`

`trade.csv	`

| Support | 2       | 4     | 8    | 16   | 32   | 64   |
| ------- | ------- | ----- | ---- | ---- | ---- | ---- |
| dptno   | 76249   | 1341  | 415  | 203  | 118  | 78   |
| pluno   | 5857182 | 17357 | 3338 | 1254 | 653  | 396  |
| bndno   | 4884    | 465   | 190  | 103  | 70   | 53   |

`trade_new.csv`

| Support | 2       | 4     | 8     | 16   | 32   | 64   |
| ------- | ------- | ----- | ----- | ---- | ---- | ---- |
| dptno   | 90509   | 3786  | 1272  | 635  | 398  | 262  |
| pluno   | 2540013 | 41708 | 11417 | 5287 | 2819 | 1758 |
| bndno   | 51770   | 3387  | 1266  | 695  | 423  | 292  |

- `pattern数`随着 `support`增大而减小，由于`support`表示支持度，支持度越低，符合的`pattern数`越多
- 相对于`ai`各个`support`对应的`pattern数`都变大了，由于将一个用户的多个订单组合，则各个`item`之间的组合次数也增多了

## 3 性能比较

![4D456A308E33537F52FFB076D5833112](/Users/yigritte/Desktop/4D456A308E33537F52FFB076D5833112.png)

