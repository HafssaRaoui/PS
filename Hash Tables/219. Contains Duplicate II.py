class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        map = {}
        for index,num in enumerate(nums):

            if num in map and index - map[num] <= k :
                return True
            
            map[num] = index
        
        return False