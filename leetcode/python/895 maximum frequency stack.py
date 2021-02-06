## 题目描述

```
实现 FreqStack，模拟类似栈的数据结构的操作的一个类。

FreqStack 有两个函数：

push(int x)，将整数 x 推入栈中。
pop()，它移除并返回栈中出现最频繁的元素。
如果最频繁的元素不只一个，则移除并返回最接近栈顶的元素。
 

示例：

输入：
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
输出：[null,null,null,null,null,null,null,5,7,5,4]
解释：
执行六次 .push 操作后，栈自底向上为 [5,7,5,7,4,5]。然后：

pop() -> 返回 5，因为 5 是出现频率最高的。
栈变成 [5,7,5,7,4]。

pop() -> 返回 7，因为 5 和 7 都是频率最高的，但 7 最接近栈顶。
栈变成 [5,7,5,4]。

pop() -> 返回 5 。
栈变成 [5,7,4]。

pop() -> 返回 4 。
栈变成 [5,7]。
 

提示：

对 FreqStack.push(int x) 的调用中 0 <= x <= 10^9。
如果栈的元素数目为零，则保证不会调用  FreqStack.pop()。
单个测试样例中，对 FreqStack.push 的总调用次数不会超过 10000。
单个测试样例中，对 FreqStack.pop 的总调用次数不会超过 10000。
所有测试样例中，对 FreqStack.push 和 FreqStack.pop 的总调用次数不会超过 150000。

```

## 前置知识

- 栈
- 哈希表



## 关键点解析

- 栈的基本性质
- hashtable的基本性质
- push和pop的时候同时更新fraq，max_fraq 和 fraq_stack。

## 代码

```python
class FreqStack:

    def __init__(self):
        self.fraq = collections.defaultdict(lambda: 0)
        self.fraq_stack = collections.defaultdict(list)
        self.max_fraq = 0
        
    def push(self, x: int) -> None:
        self.fraq[x] += 1
        if self.fraq[x] > self.max_fraq:
            self.max_fraq = self.fraq[x]
        self.fraq_stack[self.fraq[x]].append(x)    
        
    def pop(self) -> int:
        ans = self.fraq_stack[self.max_fraq].pop()
        self.fraq[ans] -= 1
        if not self.fraq_stack[self.max_fraq]:
            self.max_fraq -= 1
        return ans

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
```