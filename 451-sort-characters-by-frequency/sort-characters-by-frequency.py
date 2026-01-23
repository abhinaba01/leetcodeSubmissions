class Solution:
    def frequencySort(self, s: str) -> str:

        freq = Counter(s)
        maxHeap = []
        s1 = ""

        for ch in s:
            heapq.heappush_max(maxHeap,(freq[ch],ch))

        while maxHeap:
            cnt , ch = heapq.heappop_max(maxHeap)
            s1 += ch
        return s1
        