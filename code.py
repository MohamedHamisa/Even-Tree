class Graph:
    def __init__(self, n, t_from, t_to):
        self.n_nodes = n
        self.adj_list = {i:set() for i in range(n)}
        for w, v in zip(t_from, t_to):
            self.adj_list[w-1].add(v-1)
            self.adj_list[v-1].add(w-1)
        self.out = 0

    def dfs(self, v, p):        
        s = (1 + sum(self.dfs(w, v) for w in self.adj_list[v] if w != p)) % 2    
        self.out += not s           
        return s
               

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    g = Graph(t_nodes, t_from, t_to)
    g.dfs(0, 0)
    return g.out-1

