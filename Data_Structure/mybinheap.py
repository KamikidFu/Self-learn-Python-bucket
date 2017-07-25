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
        while(i*2) <= self.currentSize:
            mc = self.min_child(i)
            if self.heap[i] > self.heap[mc]:
                temp = self.heap[i]
                self.heap[i] = self.heap[mc]
                self.heap[mc] = temp
            i = mc

    def min_child(self, i):
        if i*2 + 1 > self.currentSize:
            return i*2
        else:
            if self.heap[i*2] < self.heap[i*2+1]:
                return i*2
            else:
                return i*2 +1 

    def del_min(self):
        retval = self.heap[1]
        self.heap[1] = self.heap[self.currentSize]
        self.currentSize = self.currentSize -1
        self.heap.pop()
        self.key_down_map(1)
        return retval
            

    def insert(self, key):
        self.heap.append(key)
        self.currentSize += 1
        self.key_up_map(self.currentSize)

    
            
