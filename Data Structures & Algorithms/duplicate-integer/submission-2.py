class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        trackingDict = {}
        for n in nums:
            if len(trackingDict) == 0 or n not in trackingDict:
                trackingDict[n] = 1
            elif n in trackingDict.keys():
                return True
        return False
