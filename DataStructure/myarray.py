import ctypes
import sys
	 
class DynamicArray(object):
              
    def __init__(self):
        self._count = 0
        self._capacity = 1
        self._array = self.make_array(self._capacity)
              
    def __len__(self):
        return self._count
              
    def __getitem__(self,key):
        if not 0 <= key < self.count:
            return IndexError('Key is out of bounds!')
        return self._array[key]

    def print_array(self):
        for i in range(self._count):
            print(self._array[i])
    
    def append(self,data):
        if self._count == self._capacity:
            self._resize(2*self._capacity) # 2x if capacity isn't enough
        self._array[self._count] = data
        self._count += 1
        
    def delete_by_data(self,data):
        index = 0
        for i in range(self._count):
            if(self._array[i] != data):
                index += 1
            else:
                break

        for i in range(self._count - index - 1):
            if i+index+1 < self._count:
                self._array[i+index] = self._array[i+index+1]

        self._count -= 1

    def has_data(self,data):
        for i in range(self._count):
            if(self._array[i] == data):
                return True

        return False
    
    def _resize(self,new_cap):
        new_array = self.make_array(new_cap)
                
        for key in range(self._count):
            new_array[key] = self._array[key]
                
        self._array = new_array
        self._capacity = new_cap
              
    def make_array(self,new_cap):
        return (new_cap*ctypes.py_object)()
