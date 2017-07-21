class GraphAdjacentMatrix():
    def __init__(self, vertex_length, graph_type):
        if(vertex_length>0 and (graph_type=="Directed" or graph_type=="Undirected" or graph_type == "Network")):
            self._enable=1
            self._graph_type = graph_type
            self._vertex_length = [i for i in range(vertex_length)]
            if(graph_type != "Network"):
                self._vertex_edges = [[0 for i in range(vertex_length)] for i in range(vertex_length)]
            else:
                self._vertex_edges = [[-1 for i in range(vertex_length)] for i in range(vertex_length)]
        else:
            self._enable=0
            print("Initial object error.\n")

    def set_edge(self, vertex_from, vertex_to, edge):
        if(self._graph_type == "Undirected"):
            if(vertex_from!=vertex_to):
                self._vertex_edges[vertex_from][vertex_to]=edge
                self._vertex_edges[vertex_to][vertex_from]=edge
            else:
                print("In undirected graph, vertex can not be self-point.")
        else:
            self._vertex_edges[vertex_from][vertex_to]=edge          
        
    def show_graph(self):
        temp="\t"
        for item in range(len(self._vertex_length)):
            temp += (str(self._vertex_length[item])+"\t")
        print(temp)
        for row in range(len(self._vertex_edges)):
            temp=(str(row)+"\t")
            for column in range(len(self._vertex_edges)):
                temp+=(str(self._vertex_edges[row][column])+"\t")
            print(temp)
            
    def show_graph_edge(self):
        temp=""
        for row in range(len(self._vertex_edges)):
            for column in range(len(self._vertex_edges)):
                temp+=(str(self._vertex_edges[row][column])+"\t")
            print(temp)
            temp=""

    def show_graph_vertex(self):
        temp="Vertex(s): "
        for item in range(len(self._vertex_length)):
            temp += (str(self._vertex_length[item])+"\t")
        print(temp)
            
