
# coding: utf-8

# Task01：数组（1天）
# >https://github.com/datawhalechina/team-learning/blob/master/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E4%B8%8E%E7%AE%97%E6%B3%95%EF%BC%88%E4%B8%8A%EF%BC%89/1_%E6%95%B0%E7%BB%84.md

# In[3]:


import ctypes


# In[30]:


#函数上会标明该方法的时间复杂度
#动态数组的类

class DynamicArray:
    
    def __init__ (self, capacity = 10):
        'Create an empty array.'
        self._n = 0 #size  当前数组的大小
        self._capacity = capacity    #先给个10  整个数组的容量
        self._A = self._make_array(self._capacity)  # 给数组分配对应 self._capacity 大小的地址空间， 可索引
        
    def __len__ (self):
        return self._n
    
    def is_empty(self):
        return self._n == 0
    
    # O(1)
    def __getitem__ (self, k): # 获取对应索引的值
        if not 0 <= k < self._n:
            raise ValueError('invalid index') 
        return self._A[k]
       
    # O(1) 
    def append(self, obj): # 在数组末尾添加值
        if self._n == self._capacity:    #首先要判断该容器是否放得下
            self._resize(2 * self._capacity)
        self._A[self._n] = obj    
        self._n += 1
        
    def _make_array(self, c):
        return (c * ctypes.py_object)( ) # 分配地址空间
    
    def _resize(self, c): # 重新分配数组地址空间， 同时将原地址空间的内容赋值到新的地址空间
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c   

    # O(n)
    def insert(self, k, value): # 在数组特定索引增加一个元素，从后往前将索引后的数据往后移动
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):    #从后往前一个一个往后移
            self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1
     
    # O(n)    
    def remove(self, value): # 移除特定元素，所有的
        for k in range(self._n):
            if self._A[k] == value:     #一个个查value
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j+1]   ##再一个个移上来
                self._A[self._n - 1] = None
                self._n -= 1
                return
        raise ValueError( 'value not found' )
    
    def _print(self):
        for i in range(self._n):
            print(self._A[i], end = ' ')
        print()


# In[34]:


list(range(1, 10+1, 1))


# **1 利用动态数组解决数据存放问题**
# > 编写一段代码，要求输入一个整数N，用动态数组A来存放2~N之间所有5或7的倍数，输出该数组。

# In[37]:


# 利用动态数组解决数据存放问题
N = 120
dyList = DynamicArray(20)
for i in range(1, N+1, 1):
    if i%5 == 0 or i % 7 == 0:
        dyList.append(i)
dyList._print()


# In[50]:


matrix[0][0]


# **2. 托普利茨矩阵问题**
# > 如果一个矩阵的每一方向由左上到右下的对角线上具有相同元素，那么这个矩阵是托普利茨矩阵。
# > 给定一个M x N的矩阵，当且仅当它是托普利茨矩阵时返回True。

# In[51]:


# 托普利茨矩阵问题

def isToeplitz(matrix):
    row = len(matrix)
    col = len(matrix[0])
    
    for c in range(col):
        item = matrix[0][c]
        for r in range(row):
            col_index = c + r
            if col_index >= col:
                break
            if item != matrix[r][col_index]:
                return False
    for r in range(1, row):
        item = matrix[r][0]
        for c in range(col-1):
            row_index = c + r
            if row_index >= row:
                break
            if item != matrix[row_index][c]:
                return False
            
    return True


# In[65]:


matrix = [[1,2,3,4,6], [5,1,2,3,4],[9,5,1,2,3]]
isToeplitz(matrix)


# **3 三数之和**
# > 给定一个包含 n 个整数的数组nums，判断nums中是否存在三个元素a，b，c，使得a + b + c = 0？找出所有满足条件且不重复的三元组。
# 
# >>* 1、 不能去重，可能存在2 -1 -1这样的元组；
# >>* 2、 可以先排序，这样可以减少部分遍历；
# >>* 3、 三重循环。

# In[75]:


nums = [-1, 0, 1, 2, -1, -4]
nums.append(5)
nums


# In[112]:


def threeSum(nums):
    nums.sort()
    res, k = [], 0
    for k in range(len(nums) - 2):
        if nums[k] > 0: break # 1. because of j > i > k.
        if k > 0 and nums[k] == nums[k - 1]: continue # 2. skip the same `nums[k]`.
        i, j = k + 1, len(nums) - 1
        while i < j: # 3. double pointer
            s = nums[k] + nums[i] + nums[j]
            if s < 0:
                i += 1
                while i < j and nums[i] == nums[i - 1]: i += 1
            elif s > 0:
                j -= 1
                while i < j and nums[j] == nums[j + 1]: j -= 1
            else:
                res.append([nums[k], nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i - 1]: i += 1
                while i < j and nums[j] == nums[j + 1]: j -= 1
    return res
# In[111]:


nums = [-1, 0, 1, 2, -1, -4]
threeNums(nums)

