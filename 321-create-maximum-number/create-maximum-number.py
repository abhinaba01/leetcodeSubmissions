class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        n1 = len(nums1)
        n2 = len(nums2)

        def maxSubsequence(l,arr):

            stack = []
            drop = len(arr) - l

            for curr in arr:
                while drop and stack and stack[-1] < curr:
                    stack.pop()
                    drop -= 1
                stack.append(curr)

            
            return stack[:l]

        def merge(seq1,seq2):
            
            i , j = 0 , 0
            res = []

            while i < len(seq1) and j < len(seq2):

                if seq1[i:] > seq2[j:]:
                    res.append(seq1[i])
                    i += 1
                else:
                    res.append(seq2[j])
                    j += 1

           
            res.extend(seq2[j:])
        
            res.extend(seq1[i:])

            return res

        ans = [0] * k
        
        for i in range(max(0, k - n2), min(k, n1) + 1):
            s1 = maxSubsequence(i,nums1)
            s2 = maxSubsequence(k - i,nums2)
            
            ans = max(ans,merge(s1,s2))

        
        return ans



            


                



            









                

       
                



           
                  
            


          

            







        

        

       
        
        