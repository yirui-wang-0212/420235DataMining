# ai

## 1 代码运行结果拷贝

结果见``ai/Output``目录下文件

![C597AE38-6377-4273-BCBA-DA7BD0FB9AFE](/Users/yigritte/Library/Containers/com.tencent.qq/Data/Library/Application Support/QQ/Users/695834367/QQ/Temp.db/C597AE38-6377-4273-BCBA-DA7BD0FB9AFE.png)

![image-20180506203709821](/var/folders/k0/973jdnld69s9y260lpyk5xww0000gn/T/abnerworks.Typora/image-20180506203709821.png)

## 2 讨论分析

`关于pattern数`

`trade.csv	`

| Support | 2    | 4    | 8    | 16   | 32   | 64   |
| ------- | ---- | ---- | ---- | ---- | ---- | ---- |
| dptno   | 2420 | 455  | 138  | 53   | 21   | 7    |
| pluno   | 4430 | 896  | 293  | 110  | 38   | 14   |
| bndno   | 921  | 236  | 77   | 29   | 10   | 5    |

`trade_new.csv`

| Support | 2     | 4    | 8    | 16   | 32   | 64   |
| ------- | ----- | ---- | ---- | ---- | ---- | ---- |
| dptno   | 4779  | 1001 | 326  | 112  | 41   | 11   |
| pluno   | 12661 | 2406 | 762  | 283  | 109  | 37   |
| bndno   | 3271  | 762  | 260  | 106  | 34   | 12   |

`pattern数`随着 `support`增大而减小，由于`support`表示支持度，支持度越低，符合的`pattern数`越多

## 3 性能比较图表

![C2494B05A5DCCE27C41DBE9B6A53A096](/Users/yigritte/Desktop/C2494B05A5DCCE27C41DBE9B6A53A096.png)