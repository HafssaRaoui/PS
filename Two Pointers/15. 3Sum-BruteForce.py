class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        triplets = set()  #only accepts hashable immutable types

        n = len(nums)

        for i in range(n-2):
            for j in range(n-1):
                for k in range(n):

                    if nums[i]+nums[j]+nums[k] == 0 :

                        triplet = (nums[i],nums[j],nums[k])
                        triplets.add(triplet)
        


        return [list(triplet) for triplet in triplets]


# Time O(n^3)  = where n is the len(nums) , comes from 3 nested loops
# Space O(m)  = m number of unique triplets stored in the set