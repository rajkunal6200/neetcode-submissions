class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp={}
        for i in range (len(s)):
            if s[i] in mp:
                mp[s[i]]+=1
            else:
                mp[s[i]]=1
        for i in range (len(s)):
            if mp[s[i]]==1:
                return i
        return -1                        