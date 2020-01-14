
# coding: utf-8

# In[1]:


#1. 无重复字符的最长子串
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = ''
        mx = 0
        #遍历整个字符串
        for c in s:
            # 判断字符是否在窗口内
            if c not in seen:
            # 如果没在窗口内 则加入窗口
                seen+=c
            # 如果字符在窗口内，则出队列到字符c后一个位置，同时将c字符入队
            else:
                seen = seen[seen.index(c) + 1:] + c
            # 取c入窗口前后的 窗口大小，取最大值
            mx = max(mx, len(seen))
        return mx


# In[3]:


solution1 = Solution()
strArr = ["abcabcbb", "bbbbb", "pwwkew"]
for item in strArr:
    print(solution1.lengthOfLongestSubstring(item))


# In[6]:


# 2. 串联所有单词的子串
from collections import Counter
class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        if n < one_word:
            return []
        words = Counter(words)
        res = []
        for i in range(0, one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                if w not in words:
                    left = right
                    cur_Counter.clear()
                    cur_cnt = 0
                else:
                    cur_Counter[w] += 1
                    cur_cnt += 1
                    while cur_Counter[w] > words[w]:
                        left_w = s[left:left+one_word]
                        left += one_word
                        cur_Counter[left_w] -= 1
                        cur_cnt -= 1
                    if cur_cnt == word_num :
                        res.append(left)
        return res


# In[10]:


solution2 = Solution()
words = [("barfoothefoobarman", ["foo","bar"]), ("wordgoodgoodgoodbestword", ["word","good","best","word"])]
for item in words:
    print(solution2.findSubstring(item[0], item[1]))


# In[12]:


from collections import Counter
words = Counter(["foo","bar"])


# In[18]:


# 3. 替换子串得到平衡字符串.
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        b = n // 4
        from collections import Counter
        counter = Counter(s)
        counter = {key:value for key,value in counter.items() if value > b}  # 转成字典， 方便索引
        if not counter or n < 4:
            return 0
        rmove = True
        l,r = 0,0
        minlen = n
        while l <= r and r < n:
            if s[r] in counter and rmove:
                counter[s[r]] -= 1
            elif l > 0 and s[l - 1] in counter and not rmove:
                counter[s[l - 1]] += 1
            if {key:value for key,value in counter.items() if value > b}:
                r += 1
                rmove = True
            else:
                minlen = min(minlen, r - l + 1)
                l += 1
                rmove = False
                         
        return minlen


# In[19]:


solution3 = Solution()
words = ["QWER", "QQWE", "QQQW", "QQQQ"]
for item in words:
    print(solution3.balancedString(item))

