
# coding: utf-8

# In[26]:


## 1、用数组实现一个顺序栈
class IStack:
    
    def __init__ (self):
        self._len = 0
        self._arr = [] # 初始化空数组
    # <summary>
    # 获取栈中实际包含元素的个数
    # </summary>
    def length(self):
        return self._len

    #<summary>
    # 获取栈顶元素
    #</summary>
    def stackTop(self):
        if self._len <= 0:
            raise IndentationError("链表为空")
        return self._arr[-1]

    # <summary>
    # 数据元素入栈
    # </summary>
    def push(self, data):
        self._arr.append(data)
        self._len += 1

    # <summary>
    # 数据元素出栈
    # </summary>
    def pop(self):
        if self._len <= 0:
            raise Exception("链表为空")
        item = self._arr.pop()
        self._len -= 1
        return item

    # <summary>
    # 判断栈中是否包含元素
    # </summary>
    # <returns>如果包含元素返回false,否则返回true.</returns>
    def isempty(self):
        if self._len <= 0:
            return True
        else:
            return False

    # <summary>
    # 从栈中移除所有元素
    # </summary>
    def Clear(self):
        for item in range(self._len):
            self._arr.pop()
        self._len = 0


# In[52]:


class ListNode(object): # 预定义链表类
    def __init__(self, x):
        self.val = x
        self.next = None


# In[53]:


# 用链表实现一个链栈
class LinkedStack:
    def __init__ (self):
        self._arr = None # 初始化链表头
        self._len = 0
    # <summary>
    # 获取栈中实际包含元素的个数
    # </summary>
    def length(self):
        return self._len

    #<summary>
    # 获取栈顶元素
    #</summary>
    def top(self):
        if self._len <= 0:
            raise IndentationError("链表为空")
        return self._arr

    # <summary>
    # 数据元素入栈
    # </summary>
    def push(self, data):
        node = ListNode(data)
        if self._len == 0:
            self._len += 1
            return node
        else:
            node.next = self._arr
        self._len += 1
        return node
    
    # <summary>
    # 数据元素出栈
    # </summary>
    def pop(self):
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
    def isempty(self):
        if self._len <= 0:
            return True
        else:
            return False

    # <summary>
    # 从栈中移除所有元素
    # </summary>
    def Clear(self):
        self._arr = None # 将链表头置空
        self._len = 0


# In[54]:


# 阶乘
n  = 5
for i in range(1, n):
    n *= i
print(n)


# In[55]:


# 斐波那契数列
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
print(fact(5)) # 120


# In[56]:


# 参考连接
# https://github.com/shiinerise/DataStructuresAndAlgorithms/blob/master/3_%E6%A0%88.md


# In[57]:

def output(stacks, n):
    global minVal, minStack
    stacks[minStack].pop()
    print('移动车厢 %d 从缓冲铁轨 %d 到出轨。' % (minVal, minStack))
    minVal = n + 2
    minStack = -1
    for index, stack in enumerate(stacks):
        if((not stack.isempty()) and (stack.top() < minVal)):
            minVal = stack.top()
            minStack = index

def inputStack(i, stacks, n):
    global minVal, minStack
    beskStack = -1  # 最小车厢索引值所在的缓冲铁轨编号
    bestTop = n + 1  # 缓冲铁轨中的最小车厢编号
    for index, stack in enumerate(stacks):
        if not stack.isempty():  # 若缓冲铁轨不为空
            # 若缓冲铁轨的栈顶元素大于要放入缓冲铁轨的元素，并且其栈顶元素小于当前缓冲铁轨中的最小编号
            a = stack.top()
            # print('stack.top()的类型是', a)
            if (a > i and bestTop > a):
                bestTop = stack.top()
                beskStack = index
        else:  # 若缓冲铁轨为空
            if beskStack == -1:
                beskStack = index
                break
    if beskStack == -1:
        return False
    stacks[beskStack].push(i)
    print('移动车厢 %d 从入轨到缓冲铁轨 %d。' % (i, beskStack))
    if i < minVal:
        minVal = i
        minStack = beskStack
    return True

def rail_road(list, k):
    global minVal, minStack
    stacks = []
    for i in range(k):
        stack = LinkedStack()
        stacks.append(stack)
    nowNeed = 1
    n = len(list)
    minVal = n + 1
    minStack = -1
    for i in list:
        if i == nowNeed:
            print('移动车厢 %d 从入轨到出轨。' % i)
            nowNeed += 1
            # print("minVal", minVal)
            while (minVal == nowNeed):
                output(stacks, n)  # 在缓冲栈中查找是否有需求值
                nowNeed += 1
        else:
            if(inputStack(i, stacks, n) == False):
                return False
    return True


