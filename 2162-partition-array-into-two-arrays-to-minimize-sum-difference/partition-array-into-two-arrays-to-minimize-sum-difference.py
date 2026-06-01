class Solution:
    def minimumDifference(self, nums: List[int]) -> int:

        n = len(nums)
        total = sum(nums)

        INF = float("inf")

        target = total / 2
        mid = n // 2

        dp1 , dp2 = {} , {}

        def calc(arr):

            res = defaultdict(list)
            n = len(arr)



            def solve(i,total,k):

                if  i == len(arr):
                    res[k].append(total)
                    return
                    
                solve(i + 1, total + arr[i],k + 1)

                solve(i + 1, total , k)

            solve(0,0,0)

            return res


        dp1 = calc(nums[:mid])
        dp2 = calc(nums[mid:])

        dp1[0] = [0]
        dp2[0] = [0]

        



        

        
        
        ansk = [0] * (mid + 1)
        for k in range(mid + 1):

            arr1 = dp1[k]
            arr2 = dp2[mid - k]

            arr1.sort()
            arr2.sort()

          
            res = INF

            ansi = [0] * len(arr1)
            for i in range(len(arr1)):

                x = target - arr1[i]

                low , high = 0 , len(arr2) - 1

                prev , nxt = None , None
                
                pos = bisect_right(arr2,x)-1 # bisect_right checks for first pos with value > x

                if pos != 0:
                    prev = arr2[pos]

                pos = bisect_left(arr2,x) # bisect_left checks  for first pos with value >= x

                if pos != len(arr2):
                    nxt = arr2[pos]

                best = INF

                if prev is not None :
                    best = min(
                        best,
                        abs(total - 2 * (arr1[i] + prev))
                    )

                if nxt is not None :
                    best = min(
                        best,
                        abs(total - 2 * (arr1[i] + nxt))
                    )

                ansi[i] = best

            
            ansk[k] = min(ansi)

        return min(ansk)

            

            






                    

                

            



                






            

        



                
                    


            
        