from collections import defaultdict

def topological_sort_dfs(graph):
    adj = defaultdict(list)
    nodes = set()
    topological_order_stack = []

    for u, neighbors in graph.items():
        nodes.add(u)
        for v in neighbors:
            adj[u].append(v)
            nodes.add(v)
    visited_states = defaultdict(int)

    def dfs_visit(u):
        visited_states[u] = 1 #start visiting
        for v in adj[u]:
            if visited_states[v] == 1:
                raise ValueError("graph has a cycle")
            if visited_states[v] == 0:
                dfs_visited(v)
        visited_states = 2 # finish visiting
        top_order_stack.append(u)

    for node in nodes:
        if visited_states[node] == 0:
            dfs_visit(node)

    return top_order_stack[::-1]
