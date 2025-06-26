class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix = [1]*n
        suf=1

        for i in range(1,n):
            prefix[i] = nums[i-1]*prefix [i-1]

        for i in range(n-1,-1,-1):
            prefix[i]*=suf
            suf*=nums[i]


        return prefix