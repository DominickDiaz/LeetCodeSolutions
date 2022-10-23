class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = 0
        lst = []
        
        for i in range(len(s)):
            count = 0
            for j in range(i, len(s)):
                if s[j] not in lst:
                    lst.append(s[j])
                    count += 1
                    maxCount = max(maxCount, count)
                else:
                    lst.clear()
                    break
        return maxCount