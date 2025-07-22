class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        if not nums :
            return 0
        
        nums_set = set(nums)
        longest_streak = 1

        for num in nums_set :

            #if it is a  beginning of a sequence
            if num -1 not in nums_set :

                current_streak = 1
                current_num = num 

                while current_num +1 in nums_set :
                    current_streak+=1
                    current_num+=1
                
                longest_streak = max(longest_streak,current_streak)
        
        return longest_streak
    

#Time Complexity: O(n), as each loop iteration that triggers a search costs at most the length of the sequence, and the whole process comprises O(n) numbers.
#Space Complexity: O(n), as we store all numbers in a set.
