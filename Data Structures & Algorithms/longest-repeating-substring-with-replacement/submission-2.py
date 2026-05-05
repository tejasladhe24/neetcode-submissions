class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0;
        max_len=0;
        freq = {}

        for r,elem in enumerate(s):
            freq[elem] = freq.get(elem,0)+1
            max_freq = max(freq.values())
            if r-l+1 > max_freq+k:
                freq[s[l]] -= 1
                l+=1
            
            max_len = max(max_len,r-l+1)

        return max_len