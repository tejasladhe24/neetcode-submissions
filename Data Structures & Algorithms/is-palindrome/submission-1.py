class Solution:
    def __init__(self) -> None:
        valid_keys = [chr(i+97) for i in range(26)] + [str(i) for i in range(10)]
        print(valid_keys)
        self.valid = {}

        for elem in valid_keys:
            self.valid[elem] = True


    def is_valid(self, elem, case_sensitive=False):
        if case_sensitive:
            return elem in self.valid
        return elem.lower() in self.valid

    def isPalindrome(self, s: str) -> bool:
        # s = "".join([elem.lower() for elem in s if elem.isalnum()])
        s = "".join([elem.lower() for elem in s if self.is_valid(elem)])
        l,r=0,len(s)-1

        while l<r:
            print(s[l],s[r])
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        
        return True