import heapq
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:

        if not self.minHeap:
            heapq.heappush(self.minHeap, -num)
        elif num <= -self.minHeap[0]:
            heapq.heappush(self.minHeap, -num)
        else:
            heapq.heappush(self.maxHeap, num)


        if len(self.minHeap) > len(self.maxHeap) + 1:
            temp = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -temp)
        elif len(self.minHeap) +1 < len(self.maxHeap) + 1:
            temp = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -temp)

            

    def findMedian(self) -> float:

        if len(self.minHeap) == len(self.maxHeap):
            small = -self.minHeap[0]
            big = self.maxHeap[0]

            return (small + big) /2
        elif len(self.minHeap) > len(self.maxHeap):
            return -self.minHeap[0]
        else:
            return self.maxHeap[0]
        
        
        