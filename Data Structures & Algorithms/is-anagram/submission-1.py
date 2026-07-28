class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        trackingDict = {}
        for val in s:
            if val in trackingDict :
                trackingDict[val] = trackingDict[val]+1
            else:
                trackingDict[val] = 1
        for val in t:
            if val not in trackingDict:
                return False
            else:
                trackingDict[val] = trackingDict[val]-1
                if trackingDict[val] < 0:
                    return False
        return True