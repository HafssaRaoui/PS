#Instant idea involves the use of a hashmap
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        map={}

        for num in nums:
            if num in map :
                map[num]+=1
            else :
                map[num]=1
        
            
        ans = -1 
        max_count = -1 
        for key,val in map.items():
            if val > max_count:
                max_count = val
                ans = key
        
        return ans