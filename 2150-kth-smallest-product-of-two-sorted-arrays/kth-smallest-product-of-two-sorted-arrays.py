class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:

        


        nums1.sort()
        nums2.sort()

        n1 , n2 = len(nums1) , len(nums2)

        ans  = -1

        def f(val):

            cnt = 0
            for i in range(n1):

                if nums1[i] == 0:
                    if val >= 0:
                        cnt += n2
                    
                    
                else:
                    
                    if nums1[i] < 0:
                        target = -(-val // nums1[i])
                        idx = bisect_left(nums2, target)

                        cnt += (n2 - idx)
                       
                    else:
                        cnt += bisect_right(nums2,val//nums1[i])
                

            return cnt >= k
                
            


        low = min(nums1[0] * nums2[0] , nums1[0] * nums2[-1] , nums1[-1] * nums2[0] , nums1[-1] * nums2[-1])
        high = max(nums1[0] * nums2[0] , nums1[0] * nums2[-1] , nums1[-1] * nums2[0] , nums1[-1] * nums2[-1])

        ans  = -1

      

        while low <= high:
            mid = low + (high - low) // 2
            
            if f(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        
        return ans

