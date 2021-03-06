## 题目描述

```
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

```

## 思路

根据题目描述，由于加上了时间复杂度必须是 O(n)，并且空间复杂度为 O(1)的条件，因此不能用排序方法，也不能使用 map 数据结构。

我们可以利用二进制异或的性质来完成，将所有数字异或即得到唯一出现的数字。

## 关键点

1. 异或的性质
   两个数字异或的结果`a^b`是将 a 和 b 的二进制每一位进行运算，得出的数字。 运算的逻辑是
   如果同一位的数字相同则为 0，不同则为 1

2. 异或的规律

- 任何数和本身异或则为`0`

- 任何数和 0 异或是`本身`

3. 很多人只是记得异或的性质和规律，但是缺乏对其本质的理解，导致很难想到这种解法（我本人也没想到）

4. bit 运算



// LeetCode, Single Number
// 时间复杂度O(n)，空间复杂度O(1)
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int x = 0;
        for (auto i : nums) {
            x ^= i;
        }
        return x;
    }
};




// LeetCode, Single Number
// 时间复杂度O(n)，空间复杂度O(1)
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        return accumulate(nums.begin(), nums.end(), 0, bit_xor<int>());
    }
};



#AZL

C Code：

```C
int singleNumber(int* nums, int numsSize){
    int res=0;
    for(int i=0;i<numsSize;i++)
    {
        res ^= nums[i];
    }
    
    return res;
}
```

C++ Code：
```C++
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        auto ret = 0;
        for (auto i : nums) ret ^= i;
        return ret;
    }
};

// C++ one-liner
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        return accumulate(nums.cbegin(), nums.cend(), 0, bit_xor<int>());
    }
};
```