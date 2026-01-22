class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        n = len(nums2)

        stack = []
        nge = defaultdict(lambda:-1)

        for i in range(n):

            while stack and nums2[i] > nums2[stack[-1]]:
                nge[nums2[stack[-1]]] = nums2[i]
                stack.pop()

            stack.append(i)

        res = []
        
        for num in nums1:
            res.append(nge[num])
        
        return res


        
        