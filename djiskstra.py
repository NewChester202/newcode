from heapq import heappop, heappush
from math import inf

key_to_graph = {
    'A': 'Restaurant',
    'B': "Barbeque",
    'C': "Cafe",
    'D': "Theatre",
    'E': "Home"
}

graph = {
    'Restaurant': [['Barbeque', 1]],
    'Barbeque': [['Cafe', 1]],
    'Cafe': [['Theatre', 1]],
    'Theatre': [['Home', 1]],
    'Home': [['Restaurant', 1]]
}

def dijkstras(graph, start):
    distances = {}
    for vertex in graph:
        distances[vertex] = inf
  
    distances[start] = 0
    vertices_to_explore = [(0, start)]
    while vertices_to_explore:
        current_distance, current_vertex = heappop(vertices_to_explore)
  
        for neighbor, edge_weight in graph[current_vertex]:
            new_distance = current_distance + edge_weight
    
        if new_distance < distances[neighbor]:
            distances[neighbor] = new_distance
            heappush(vertices_to_explore, (new_distance, neighbor))
      
    return distances

def asking():
    origin = input("""where are you? enter key for location:
A. Restaurant
B. Barbeque
C. Cafe
D. Theatre
E. Home
""")
    start = key_to_graph[origin]
    distances = dijkstras(graph, start)
    endpoint = input("""where do you want to go? enter key for location:
A. Restaurant
B. Barbeque
C. Cafe
D. Theatre
E. Home
""")
    end = key_to_graph[endpoint]
    distance = distances[end]
    print(f"it takes {distance} hours to get there")


asking()
