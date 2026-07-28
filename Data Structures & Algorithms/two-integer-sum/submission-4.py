class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []
        #hashMap = {}
        #if len(nums)==2:
        #    return [0,1]
        #for i in range(len(nums)):
        #    if nums[i] in hashMap.values():
        #        return [nums.index(target-nums[i]), i]
        #    hashMap[nums[i]] = target-nums[i]
