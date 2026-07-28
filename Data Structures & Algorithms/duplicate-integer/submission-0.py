class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range (0,len(nums)-1):
            for j in range (len(nums)-1,-1, -1):
                if i==j:
                    break
                if nums[i] == nums[j]:
                    return True
                else:
                    continue
        return False