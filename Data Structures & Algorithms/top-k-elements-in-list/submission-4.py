class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        trackingDict = {}

        for num in nums:
            if num not in trackingDict:
                trackingDict[num] = 1
            else:
                trackingDict[num] += 1

        keyList = [i for i in range(1,len(nums)+1)]
        valList = [[] for i in range(0, len(nums))]
        bucketSortDict = dict(zip(keyList, valList))

        for kk in list(trackingDict.keys()):
            bucketSortDict[trackingDict[kk]].append(kk)

        
        result = []
        for key in reversed(bucketSortDict):
            if len(result) == k:
                return result
            if len(result) < k and bucketSortDict[key]:
                result.extend(bucketSortDict[key])
        return result
            
        
        
            