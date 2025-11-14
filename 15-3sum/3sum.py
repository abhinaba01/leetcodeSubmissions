class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:

        arr.sort()
        n = len(arr)

        ans = []

        i = 0
       

        while i < n:

            j = i + 1
            k = n - 1

            while j < k:

                s = arr[i] + arr[j] + arr[k]

                if s == 0:
                    ans.append([arr[i],arr[j],arr[k]])

                    part1 = arr[j]
                    part2 = arr[k]

                    

                    
                    while j < k and arr[j] == part1:
                            j += 1
                    while j < k and arr[k] == part2:
                            k -= 1

                elif s < 0:

                    part1 = arr[j]

                    while j < k and arr[j] == part1:
                        j += 1
                    
                else:

                    part2 = arr[k]

                    while j < k and arr[k] == part2:
                        k -= 1

            curr = arr[i]

            while i < n  and arr[i] == curr:
                i += 1

        return ans 



                

                



        




        
        