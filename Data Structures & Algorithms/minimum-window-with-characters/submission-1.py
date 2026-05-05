class Solution:

    def count_chars(self,s):
        data = {}
        for elem in s:
            data[elem] = data.get(elem,0) + 1
        return data

    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = self.count_chars(t)
        need_unique = len(need)
        have = 0
        l=0

        best_len,best_l,best_r = float("inf"),0,0

        s_map = {}

        for r,elem in enumerate(s):
            s_map[elem] = s_map.get(elem,0) + 1

            if elem in need and s_map[elem] == need[elem]:
                have+=1

            while have == need_unique:
                window_len = r-l+1
                if window_len < best_len:
                    best_len,best_l,best_r = window_len,l,r

                s_map[s[l]] -= 1
                if s[l] in need and s_map[s[l]] < need[s[l]]:
                    have -= 1
                l+=1

        return "" if best_len == float("inf") else s[best_l:best_r+1]