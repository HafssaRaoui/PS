class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = {}

        for s in strs : 

            count = [0]*26
            for char in s :
                count[ord(char)-ord("a")]+=1
            
            count = tuple(count)

            if count not in map : 
                map[count]= []
            
            map[count].append(s)
        

        return list(map.values())
    

    # Time complexity O(n*m)
    #Space complexity O(n*m) 