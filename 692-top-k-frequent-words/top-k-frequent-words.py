class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        freq = Counter(words)
        minHeap = []
        ans = []

        for key,value in freq.items():
            heapq.heappush(minHeap,(-value,key))

            
        
        while k > 0:
            cnt , word = heapq.heappop(minHeap)
            ans.append(word)
            k -= 1

         
        return ans



        
        