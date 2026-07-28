class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        if len(nums)==2:
            return [0,1]
        for i in range(len(nums)):
            if nums[i] in hashMap.values():
                return [nums.index(target-nums[i]), i]
            hashMap[nums[i]] = target-nums[i]
