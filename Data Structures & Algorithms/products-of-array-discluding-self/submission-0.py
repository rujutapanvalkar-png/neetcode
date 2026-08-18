class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preList = []
        for i in range(0,len(nums)):
            if i == 0:
                preList.append(1)
            else:
                preList.append(nums[i-1]*preList[i-1])
        
        postList = [1]*len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums)-1:
                postList[i] = 1
            else:
                postList[i] = (nums[i+1]*postList[i+1])

        return [x * y for x, y in zip(preList, postList)]