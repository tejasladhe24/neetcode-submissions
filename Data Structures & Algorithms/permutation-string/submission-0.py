class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        for elem in s1:
            s1_map[elem] = s1_map.get(elem,0)+1

        l=0; s2_map = {}
        for r,elem in enumerate(s2):
            s2_map[elem] = s2_map.get(elem,0) + 1
            while r-l+1 > len(s1):
                s2_map[s2[l]] -= 1
                if s2_map[s2[l]] == 0:
                    del s2_map[s2[l]]
                l += 1

            if s1_map == s2_map:
                return True
            
        
        return False