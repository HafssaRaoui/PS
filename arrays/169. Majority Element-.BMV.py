#Use Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        candidate = nums[0]
        count = 0 

        for num in nums:
            if count == 0 :
                candidate = num
            
            count+=1 if num==candidate else -1




        return candidate
    

#Time O(n)
#Space O(1)