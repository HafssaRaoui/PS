class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int] :

        l ,r = 0 ,len(numbers)-1

        while l < r :

            current_sum = numbers[l] + numbers[r]

            if current_sum == target :
                return [l+1,r+1]
            
            elif current_sum < target :
                l+=1
            
            else : 
                r-=1
        
        return [l+1,r+1] 
    


#Time O(n)  = each element is processed at most once

#Space O(1) = since we use fixed numbers of additional variables