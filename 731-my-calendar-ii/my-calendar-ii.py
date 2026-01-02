class MyCalendarTwo:

    def __init__(self):
        self.diff = {}
        

    def book(self, startTime: int, endTime: int) -> bool:

        self.diff[startTime] = self.diff.get(startTime, 0) + 1
        self.diff[endTime] = self.diff.get(endTime, 0) - 1

        active = 0
        for t in sorted(self.diff):
            active += self.diff[t]
            if active >= 3:
               
                self.diff[startTime] -= 1
                if self.diff[startTime] == 0:
                    del self.diff[startTime]

                self.diff[endTime] += 1
                if self.diff[endTime] == 0:
                    del self.diff[endTime]

                return False

        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)