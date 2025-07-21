class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = {}

        for s in strs : 

            sorted_s = tuple(sorted(s))  #used as a  key

            if sorted_s not in map : 
                map[sorted_s]= []
            
            map[sorted_s].append(s)
        

        return list(map.values())
    

    # Time complexity O(n*m*log(m))
    #Space complexity O(n*m) (at worst u have a dict of n keys ,each key is a tuple of m length)