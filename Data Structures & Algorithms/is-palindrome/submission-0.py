class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([elem.lower() for elem in s if elem.isalnum()])
        l,r=0,len(s)-1

        while l<r:
            print(s[l],s[r])
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        
        return True