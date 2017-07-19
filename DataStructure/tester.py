import mygraph
import mylist
import myarray
import random
import pdb
#mygraph.GraphAdjacentMaterix():
#Constructor contains two fields
#No.1 How many vertexs in graph. Range:[2,+∞), by this tester, range is [2,9]
#No.2 What is the type of graph. Directed, Undirected, Network
def test_graph_adjacent_matrix():
    vertex_length = random.randint(2,9)
    type_of_graph = {0: "Undirected",1: "Directed",2: "Network"}
    matrix = mygraph.GraphAdjacentMatrix(vertex_length, str(type_of_graph[random.randint(0,2)]))
    print("---START TESTING---\nVertexs: "+str(vertex_length)+"\nGraph Type: "+matrix._graph_type)
    if(matrix._enable !=0 ):
        print("\n---SHOW VERTEX(S)---")
        matrix.show_graph_vertex()
        
        print("\n---SHOW INITIAL GRAPH---")
        matrix.show_graph()
        
        rand1=random.randint(0,vertex_length-1)
        rand2=random.randint(0,vertex_length-1)
        print("\n---RANDOM SET EDGE OR ARC---\n---AT ("+str(rand1)+","+str(rand2)+")---")
        matrix.set_edge(rand1,rand2,1)
        
        print("\n---SHOW INITIAL GRAPH---")
        matrix.show_graph()

def test_linked_list():
    init_length_of_list = random.randint(1,9)
    print("\n---START TESTING---\nInitial Length: "+str(init_length_of_list))
    linkedlist = mylist.LinkedList(random.randint(0,99))
    for i in range(init_length_of_list):
        linkedlist.add_node(random.randint(0,99))
    print(str("Size: "+str(linkedlist.get_size())))
    
    print("---SHOW LINKEDLIST WITH INITIAL DATA---")
    linkedlist.print_list()

    print("---TEST DELETE FUNCTION WITH DATA---")
    data = input("Input the data in linked list: ")
    #pdb.set_trace()
    while True:
        if linkedlist.find_node_by_data(int(data)) != None:
            linkedlist.del_node_by_data(int(data))
            break
        else:
            data = input("Data not in linked list, retype data: ")
    print("---TEST PRINT NEW LIST AFTER DELETE "+str(data)+"---")
    linkedlist.print_list()
    
    index = random.randint(0,len(linkedlist)-1)    
    print("---TEST DELETE FUNCTION AT INDEX "+str(index)+"---")
    #pdb.set_trace()
    linkedlist.del_node_by_index(index)
    print("---TEST PRINT NEW LIST AFTER DELETE AT INDEX "+str(index)+"---")
    linkedlist.print_list()

def test_array():
    init_length_of_list = random.randint(1,9)
    print("\n---START TESTING---\nInitial Length: "+str(init_length_of_list))
    array = myarray.DynamicArray()
    for i in range(init_length_of_list):
        array.append(random.randint(0,99))

    print("---SHOW ARRAY WITH INITIAL DATA---")
    array.print_array()

    print("---TEST DELETE FUNCTION WITH DATA---")
    data = input("Input the data in array: ")
    #pdb.set_trace()
    while True:
        if array.has_data(int(data)):
            array.delete_by_data(int(data))
            break
        else:
            data = input("Data not in array, retype data: ")
    print("---TEST PRINT NEW ARRAY AFTER DELETE "+str(data)+"---")
    array.print_array()

test_graph_adjacent_matrix()
test_linked_list()
test_array()
