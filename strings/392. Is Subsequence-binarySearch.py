from collections import defaultdict
from bisect import bisect_left
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        t_map = defaultdict(list)

        for index,char in enumerate(t):
            t_map[char].append(index)
        

        low = -1
        for char in s : 

            indices = t_map[char]
            pos = bisect_left(indices,low+1)

            if pos == len(indices):
                return False

            low = indices[pos]
        return True
