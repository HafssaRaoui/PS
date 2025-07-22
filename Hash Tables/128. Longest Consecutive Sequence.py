class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        if not nums :
            return 0
        

        longest_streak = 1 
        current_streak = 1 
        nums.sort()

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] :
                continue

            elif nums[i] == nums[i-1]+1:
                current_streak += 1
            
            else :
                longest_streak = max(longest_streak,current_streak)
                current_streak = 1 
        
        return max(longest_streak,current_streak)

#Time Complexity: O(n log n), because sorting the array takes O(n log n) and iterating through the array is O(n).
#Space Complexity: O(1) if we disregard the space used by the sort function (since it may require O(n) space).
