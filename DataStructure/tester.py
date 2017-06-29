import mygraph
import mylist
import random
    
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
    length_of_list = random.randint(1,9)
    print("\n---START TESTING---\nLength: "+str(length_of_list))
    linkedlist = mylist.LinkedList(random.randint(0,99))
    for i in range(length_of_list):
        linkedlist.add_node(random.randint(0,99))
    print(str(linkedlist.get_size()))
    print("---LINKEDLIST WITH NEW DATA---")
    linkedlist.print_list()
    
    index = random.randint(0,length_of_list)
    print("---TEST DELETE FUNCTION AT INDEX "+str(index)+"---")
    linkedlist.del_node_by_index(index)
    print("---TEST PRINT NEW LIST---")
    linkedlist.print_list()
    

test_graph_adjacent_matrix()
test_linked_list()
