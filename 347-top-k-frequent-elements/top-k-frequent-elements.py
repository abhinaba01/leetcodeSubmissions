class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)

        maxHeap = [(freq,num) for  num,freq in freq.items()]
        heapq.heapify_max(maxHeap)

        ans = []

        while k > 0:
            freq , num = heapq.heappop_max(maxHeap)
            ans.append(num)
            k -= 1

        
        return ans
            

        
        