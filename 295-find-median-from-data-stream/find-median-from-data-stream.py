class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        
        heapq.heappush_max(self.left,num)
        max_el = heapq.heappop_max(self.left)
        heapq.heappush(self.right,max_el)
        if len(self.right) > len(self.left):
            min_el = heapq.heappop(self.right)
            heapq.heappush_max(self.left,min_el)

    def findMedian(self) -> float:

        l , r = len(self.left), len(self.right)
        if (l + r) & 1 == 0:
            return (self.left[0] + self.right[0]) / 2
        else:
            return self.left[0]

       


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()