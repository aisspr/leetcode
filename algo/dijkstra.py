import heapq

class Graph:
   def __init__(self, graph: dict = {}):
       self.graph = graph

    def dijkstra(self, src):
        distances = {node: float('inf') for node in self.graph}
        distances[src] = 0
    
        if src not in self.graph:
            raise ValueError ("source not in graph")

        pq = [(0,src)] #(distance, node)
        visited = set()

        while pq:
            current_dist, current_node = heapq.heappop(pq)
            if current_node in visited:
                continue
            visited.add(current_node)
            for neighbor, weight in self.graph[current_node].items():
                tentative_dist = current_dist + weight
                if tentative_dist < distances[neighbor]: #If a shorter path to the neighbor is found
                    distances[neighbor] = tentative_dist
                    heapq.heappush(pq, (tentative_dist, neighbor))
        return distances

  
