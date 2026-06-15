class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:

        first = []
        second = []


        for rows in units:
            rows.sort()
            if len(rows) >= 2:
                second.append(rows[1])
            
            first.append(rows[0])

        
        r , c = len(units) , len(units[0])

        if c >= 2:
            return sum(second) - min(second) + min(first)
        else:
            return sum(first)


        
        