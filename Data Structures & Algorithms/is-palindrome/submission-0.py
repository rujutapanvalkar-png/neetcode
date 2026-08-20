class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0;
        j=len(s)-1
        while i < j:
            if s[i].isalnum() and s[j].isalnum() :
                if s[i].lower() == s[j].lower():
                    i = i+1
                    j=j-1
                    continue
                else:
                    return False
            elif not s[i].isalnum() and not s[j].isalnum():
                i = i+1
                j=j-1
                continue
            elif not s[i].isalnum() and s[j].isalnum():
                i=i+1
                continue
            elif s[i].isalnum() and not s[j].isalnum():
                j=j-1
                continue

        return True
                