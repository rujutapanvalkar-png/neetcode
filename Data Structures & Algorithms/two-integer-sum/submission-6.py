class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        trackingDict = {}
        for i in range(0, len(nums)):
            if nums[i] in trackingDict:
                return [trackingDict[nums[i]], i]
            else:
                trackingDict[target-nums[i]] = i
                print(trackingDict)
