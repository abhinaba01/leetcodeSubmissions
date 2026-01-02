class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        diff = defaultdict(int)

        for numPassengers,src,dst in trips:
            diff[src] += numPassengers
            diff[dst] -= numPassengers

        print(diff)

        cap = [0] * 1001
        cap[0] = diff[0]
        if cap[0] > capacity:
            return False
            

        for i in range(1,1001):
            cap[i] = cap[i-1] +  diff[i]
            if cap[i] > capacity:
                return False
        return True

        

        

        