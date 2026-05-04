class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False

        s_data = dict(); t_data = dict()
        
        for elem in s:
            s_data[elem] = s_data.get(elem,0) + 1

        for elem in t:
            t_data[elem] = t_data.get(elem,0) + 1

        for elem in list(s_data.keys()):
            if elem not in t_data:
                return False

            elif s_data[elem] != t_data[elem]:
                return False
        
        return True