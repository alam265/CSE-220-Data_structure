import heapq 
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
visited = {v:False for v in graph}

def prims(start,graph):
    Distances= {vertex:float('inf') for vertex in graph}
    visited[start] = True 
    Distances[start] = 0 
    priority_queue = [(weight, start, neighbor) for neighbor, weight in graph[start].items()]                       #implementing with list 
    mst = []
    heapq.heapify(priority_queue)
 

    while priority_queue:

        weight, v_f,v_t = heapq.heappop(priority_queue)
        if  visited[v_t]==False:
            visited[v_t] = True  
            mst.append((v_f,v_t,weight))

            for neighbor_vertex, weight in graph[v_t].items():
                    if weight < Distances[neighbor_vertex]:
                        Distances[neighbor_vertex] = weight 
                        
                        heapq.heappush(priority_queue,(weight,v_t,neighbor_vertex))
       


    return mst


source ='A'


print(prims(source,graph))











