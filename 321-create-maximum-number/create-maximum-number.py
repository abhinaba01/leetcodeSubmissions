class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        ans = []
        n = len(nums2)
        m = len(nums1)

        for i in range(max(0, k-n) , min(k, m) + 1):

            stack1 = []
            stack2 = []


            drop1 = len(nums1) - i

            for digit in nums1:
                while drop1 > 0 and stack1 and stack1[-1] < digit:
                    stack1.pop()
                    drop1 -= 1

                stack1.append(digit)

            drop2 = len(nums2) - (k - i)

            for digit in nums2:
                while drop2 > 0 and stack2 and stack2[-1] < digit:
                    stack2.pop()
                    drop2 -= 1

                stack2.append(digit)

            
            stack1 = stack1[:i]
            stack2 = stack2[:k-i]


            merged = []
            i , j = 0 , 0

            while i < len(stack1) or j < len(stack2):
                if stack1[i:] > stack2[j:]:
                    merged.append(stack1[i])
                    i += 1
                else:
                    merged.append(stack2[j])
                    j += 1

            ans = max(ans,merged)

        return ans

            
                



           
                  
            


          

            







        

        

       
        
        