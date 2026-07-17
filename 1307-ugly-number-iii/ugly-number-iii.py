class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        MAX = max(a , b , c)

        
        def f(k):

            lenA = (k) // a
            lenB = (k) // b
            lenC = (k) // c

            lenAB = (k) // lcm(a,b)
            lenAC = (k) // lcm(a,c)
            lenBC = (k) // lcm(b,c)

            lenABC = (k) // lcm(a,b,c)


            return lenA + lenB + lenC - (lenAB + lenAC + lenBC) + lenABC


        
        low , high = 1 , MAX * n
        ans = -1

        while low <= high:

            mid = (low + high) // 2

            if f(mid) < n :
                low = mid + 1
            
            elif f(mid) >= n :
                ans = mid
                high = mid - 1

           


            
        return ans





        




        
