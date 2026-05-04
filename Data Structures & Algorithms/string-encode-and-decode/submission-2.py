class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)


    def decode(self, s: str) -> List[str]:
        res: List[str] = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            n = int(s[i:j])
            i = j + 1
            res.append(s[i : i + n])
            i += n
        return res
