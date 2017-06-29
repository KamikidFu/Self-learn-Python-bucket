class LinkedList():
    def __init__(self, data):
        self._head = Node(data)
        self._count=0
        
    def __len__(self):
        return self._count

    def add_node(self, data):
        add = Node(data)
        cur = self._head
        while(cur.has_next()):
            cur = cur.get_next()
        cur.set_next(add)
        self._count+=1

    def find_node_by_data(self, data):
        cur = self._head
        while(cur.get_data()!=data):
            cur = cur.get_next()
        return cur

    def find_node_by_index(self, index):
        cur = self._head
        for i in range(index):
            cur = cur.get_next()
        return cur
    
    def del_node_by_data(self, data):
        cur = self.find_node_by_data(data)
        pre = self._head
        while(pre.get_next().get_data()==cur.get_data()):
            pre = pre.get_next()
        pre.set_next(cur.get_next())

    def del_node_by_index(self, index):
        cur = self.find_node_by_index(index)
        pre = self._head
        while(pre.get_next().get_data()==cur.get_data()):
            pre = pre.get_next()
        pre.set_next(cur.get_next())

    def print_list(self):
        output = ""
        cur = self._head
        while(cur.has_next()):
            output += (str(cur.get_data())+"\t")
            cur = cur.get_next()
        print(output)
    
    def get_size(self):
        return self._count

    
    
class Node():
    def __init__(self, data):
        self._data=data
        self._next=None
        
    def set_data(self, data):
        self._data=data

    def get_data(self):
        return self._data
    
    def set_next(self, the_next):
        self._next=the_next

    def get_next(self):
        return self._next

    def has_next(self):
        if(self._next is not None):
            return True
        return False