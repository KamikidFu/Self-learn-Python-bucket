import graph
import random
    
#Constructor contains two fields
#No.1 How many vertexs in graph. Range:[1,+∞)
#No.2 What is the type of graph. Directed, Undirected, Network
def test_adjacent_matrix(vertex_length, type_of_graph):
    print("---START TESTING---\nVertexs: "+str(vertex_length)+"\nGraph Type: "+type_of_graph)
    matrix = graph.GraphAdjacentMatrix(vertex_length, type_of_graph)
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

test_adjacent_matrix(3,"Undirected")
