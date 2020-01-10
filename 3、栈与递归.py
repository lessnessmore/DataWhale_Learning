
# coding: utf-8

# In[3]:


## 1、用数组实现一个顺序栈
class IStack:
    
    def __init__ (self, capacity):
        self._len = 0
        self._arr = [] # 初始化空数组
    # <summary>
    # 获取栈中实际包含元素的个数
    # </summary>
    def length():
        return self._len

    #<summary>
    # 获取栈顶元素
    #</summary>
    def stackTop():
        if self._len <= 0:
            raise IndentationError("链表为空")
        return self._arr[-1]

    # <summary>
    # 数据元素入栈
    # </summary>
    def push(data):
        self._arr.append(data)
        self._len += 1

    # <summary>
    # 数据元素出栈
    # </summary>
    def pop():
        if self._len <= 0:
            raise Exception("链表为空")
        item = self._arr.pop()
        self._len -= 1
        return item

    # <summary>
    # 判断栈中是否包含元素
    # </summary>
    # <returns>如果包含元素返回false,否则返回true.</returns>
    def isempty():
        if self._len <= 0:
            return True
        else:
            return False

    # <summary>
    # 从栈中移除所有元素
    # </summary>
    def Clear():
        for item in range(self._len):
            self._arr.pop()
        self._len = 0


# In[5]:


class ListNode(object): # 预定义链表类
    def __init__(self, x):
        self.val = x
        self.next = None


# In[6]:


# 用链表实现一个链栈
class LinkedStack:
    def __init__ (self, x):
        self._arr = ListNode(x) # 初始化链表头
        self._len = 1
    # <summary>
    # 获取栈中实际包含元素的个数
    # </summary>
    def length():
        return self._len

    #<summary>
    # 获取栈顶元素
    #</summary>
    def stackTop():
        if self._len <= 0:
            raise IndentationError("链表为空")
        return self._arr.val

    # <summary>
    # 数据元素入栈
    # </summary>
    def push(data):
        node = ListNode(data)
        node.next = self._arr
        self._len += 1
        return node
    
    # <summary>
    # 数据元素出栈
    # </summary>
    def pop():
        if self._len <= 0:
            raise Exception("链表为空")
        item = self._arr.val
        self._arr = self._arr.next
        self._len -= 1
        return item

    # <summary>
    # 判断栈中是否包含元素
    # </summary>
    # <returns>如果包含元素返回false,否则返回true.</returns>
    def isempty():
        if self._len <= 0:
            return True
        else:
            return False

    # <summary>
    # 从栈中移除所有元素
    # </summary>
    def Clear():
        self._arr = ListNode() # 将链表头置空
        self._len = 0


# In[8]:


# 阶乘
n  = 5
for i in range(1, n):
    n *= i
print(n)


# In[10]:


# 斐波那契数列
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
print(fact(5)) # 120


# In[20]:


# 汉诺塔
i = 0
def move(n, a, b, c):
    global i
    if (n == 1):
        i += 1
        print('移动第 {0} 次 {1} --> {2}'.format(i, a, c))
        return
    move(n - 1, a, c, b)
    move(1, a, b, c)
    move(n - 1, b, a, c)


# In[21]:


move(3, "a", "b", "c")

