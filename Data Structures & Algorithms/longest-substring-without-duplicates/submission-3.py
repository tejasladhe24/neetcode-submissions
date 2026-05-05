class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        n = len(s)
        ll = 0

        while (j<n):
            if s[j] in s[i:j]:
                i+=1
            else:
                j+=1
                ll = max(ll, j-i)
            
        return ll