class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        n = len(nums)
        i,pos = 0,0
        for i in range(n):
            if nums[i]!= 0 :
                nums[i],nums[pos] = nums[pos],nums[i]
                pos+=1



# Time O(n)
# Space O(1)