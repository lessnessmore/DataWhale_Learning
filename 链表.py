
# coding: utf-8

# In[1]:


class ListNode(object): # 预定义链表类
    def __init__(self, x):
        self.val = x
        self.next = None


# **1. 利用动态数组解决数据存放问题**

# In[2]:


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 初始化一个ListNode 最后返回的时候从链表第二个节点开始返回
        iter = ListNode(-1)
        ret = iter
        while l1 != None and l2 != None:
            if  l1.val <= l2.val:
                iter.next = l1
                l1 = l1.next
            else:
                iter.next = l2
                l2 = l2.next
            iter = iter.next
        iter.next = l1 if l1 else l2
        return ret.next
        


# In[3]:


sol = Solution()
h10 = ListNode(1)
h11 = ListNode(2)
h10.next = h11
h12 = ListNode(4)
h11.next = h12


# In[4]:


h20 = ListNode(1)
h21 = ListNode(3)
h20.next = h21
h22 = ListNode(4)
h21.next = h22
h23 = ListNode(7)
h22.next = h23


# In[5]:


sol1 = Solution()
ln1 = sol1.mergeTwoLists(h10, h20)

# **2. 删除指定节点**

# 在python2 和python3场景下区别比较大，不清楚为什么，在python2下执行耗时和耗内存都比较好，
# 尝试了双指针，效率并不比这个简单方法耗时和内存更少。
# In[6]:


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode  
        """
        arr = []  #  空间换时间
        iters = head
        while iters:
            arr.append(iters)
            iters = iters.next

        length = len(arr)
        if length == 1:
            head = None
        else:
            if n == 1:
                arr[-(n + 1)].next = None
            elif n == length:
                head = head.next
            else:
                arr[-(n + 1)].next = arr[-(n - 1)]
        return head


# In[7]:


sol2 = Solution()
ln2 = sol2.removeNthFromEnd(h10, 1)


# **3. 旋转链表**

# In[8]:


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        # 获取链表长度
        p = head
        l = 0
        while p:
            l += 1
            p = p.next

        k = k % l  # k对l取余，避免重复循环导致的超时
        if k == 0:
            return head

        pre, post = head, head
        # 让一个指针先走k步
        for i in range(k):
            post = post.next

        # 两个指针一起走，直到后面的指针指向最后一个元素
        while post.next:
            pre = pre.next
            post = post.next

        # 将链表拆分之后再反转
        tmp = pre.next
        pre.next = None
        post.next = head

        return tmp


# In[9]:


sol3 = Solution()
ln3 = sol3.rotateRight(h10, 5)

