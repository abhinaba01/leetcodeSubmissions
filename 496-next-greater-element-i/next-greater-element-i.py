class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        n1 , n2 = len(nums1) , len(nums2)
        nge = [-1] * n2
        res = []

        stack = []

        for i in range(n2):

            while stack and nums2[i] > nums2[stack[-1]]:
                index = stack.pop(-1)
                nge[index] = nums2[i]
            
            stack.append(i)

        for num in nums1:
            res.append(nge[nums2.index(num)])
        
        return res



        