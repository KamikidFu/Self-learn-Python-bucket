class LinkedList():
    def __init__(self, data):
        self._head = Node(data)
        self._count=0
        
    def __len__(self):
        return self._count
    
    def add_node_at_head(self,data):
        add = Node(data)
        add.set_next(self._head)
        self._head = add
        self._count += 1
        
    def add_node_at_tail(self, data):
        add = Node(data)
        cur = self._head
        while(cur.has_next()):
            cur = cur.get_next()
        cur.set_next(add)
        self._count+=1

    def find_node_by_data(self, data):
        cur = self._head
        while cur != None:
            if(cur.get_data() == data):
                return cur
            else:
                cur = cur.get_next()
        return None

    def find_node_by_index(self, index):
        cur = self._head
        for i in range(index):
            cur = cur.get_next()
        return cur
    
    def del_node_by_data(self, data):
        cur = self._head
        pre = None
        while cur:
            if cur.get_data() == data:
                if pre:
                    pre.set_next(cur.get_next())
                else:
                    self._head = cur
                self._count -= 1
                return
            else:
                pre = cur
                cur = cur.get_next()
        return None

    def del_node_by_index(self, index):
        cur = self._head
        pre = Node

        if index == 0:
            self._head = cur.get_next()
            return
        
        for i in range(index):
            pre = cur
            cur = cur.get_next()
        if pre:
            pre.set_next(cur.get_next())
        else:
            self._head = cur
        self._count -= 1
        return

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
