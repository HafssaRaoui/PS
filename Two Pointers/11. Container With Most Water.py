class Solution:
    def maxArea(self, height: List[int]) -> int:


        n =len(height)
        l = 0 
        r = n -1
        max_area = 0


        while l < r :

            length = min(height[l],height [r])
            width = r-l
            area = length*width

            max_area = max(max_area,area)

            if height[r] > height[l] :
                l+=1
            
            else:

                r-=1
        
        return max_area

# Time O(n)  = scan the array only once
#Space O(1)
