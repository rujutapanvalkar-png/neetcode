class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        length=0
        for n in nums:
            print(n)
            length = 1
            if n-1 not in numSet:
                while length < len(nums):
                    if n+length in numSet:
                        length=length+1
                    else:
                        break
                if length > longest:
                    longest = length

        return longest