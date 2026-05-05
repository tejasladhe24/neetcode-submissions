class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0

        i,j=0,1
        n = len(s)
        ll = 1

        while (j<n):
            if s[j] in s[i:j]:
                i+=1
            else:
                j+=1
                ll = max(ll, j-i)
            
        return ll