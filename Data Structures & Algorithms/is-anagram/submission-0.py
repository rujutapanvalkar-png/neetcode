class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = list(s)
        tt = list(t)
        if len(ss)!= len(tt):
            return False
        ss.sort()
        tt.sort()
        for i in range(0,len(ss)):
            if ss[i]!= tt[i]:
                return False
        return True