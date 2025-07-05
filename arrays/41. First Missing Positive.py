class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums.sort()
        n = len(nums)
        i = 0
        ans = 1

        while i < n and nums[i] < 1 :
            i+=1
        
        while i<n :
            if nums[i] == ans:
                ans+=1
            elif nums[i] > ans:
                return ans
            
            i+=1

        return ans
