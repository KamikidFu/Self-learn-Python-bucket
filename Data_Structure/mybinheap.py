class BinHeap(object):
    def __init__(self):
        self.heap = [0]
        self.currentSize = 0
    
    def key_up_map(self, i):
        while i//2 > 0:
            if self.heap[i] < self.heap[i//2]:
                temp = self.heap[i//2]
                self.heap[i//2]=self.heap[i]
                self.heap[i] = temp
            i = i//2

    def key_down_map(self,i):
        

    def insert(self, key):
        self.heap.append(key)
        self.currentSize += 1
        self.key_up_map(self.currentSize)

    
            
