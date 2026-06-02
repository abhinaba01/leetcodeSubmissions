class Solution:
    def minimumDifference(self, nums: List[int]) -> int:

        n = len(nums)

        total = sum(nums)
        target = total / 2
        
        mid = n // 2

        INF = float("inf")


        dp1 , dp2 = {} , {}

        def dfs(arr):

            length = len(arr)
            group = defaultdict(list)

            def f(i,totalSum,k):

                if i == length:
                    group[k].append(totalSum)
                    return

                
                f(i+1,totalSum + arr[i],k + 1)
                f(i+1,totalSum,k)

            f(0,0,0)

            return group

        
        dp1 = dfs(nums[:mid])
        dp2 = dfs(nums[mid:])

        ansk = [0] * (mid + 1)

        for k in range(mid + 1):

            arr1 = dp1[k]
            arr2 = dp2[mid-k]

            arr1.sort()
            arr2.sort()

            ansi = [0] * len(arr1)

            for i in range(len(arr1)):

                x = target - arr1[i]

                pos_right = bisect_right(arr2,x) - 1

                pos_left = bisect_left(arr2,x) 

                best = INF

                if pos_right != 0:
                    best = min(best,abs(total - 2 * (arr1[i] + arr2[pos_right])))
                
                if pos_left != len(arr2):
                    best = min(best,abs(total - 2 * (arr1[i] + arr2[pos_left])))

                ansi[i] = best

            ansk[k] = min(ansi)

        return min(ansk)



                

                

                

                    




            






                    

                

            



                






            

        



                
                    


            
        