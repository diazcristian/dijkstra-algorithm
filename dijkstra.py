import pandas as pd
import numpy as np
import heapq
import sys

def read_txt_to_adjacency_matrix(filename):
    df = pd.read_csv(filename, sep=r'\s+', header=None)
    matrix = df.values
    num_rows, num_cols = matrix.shape
    return matrix, num_rows, num_cols

def dijkstra(graph, num_vertices, start, goal):
    distances = [float('inf')] * num_vertices
    distances[start] = 0
    previous_nodes = [-1] * num_vertices
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_node == goal:
            break
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor in range(num_vertices):
            if neighbor < len(graph[current_node]) and graph[current_node][neighbor] > 0:
                distance = current_distance + graph[current_node][neighbor]
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))
    
    # Generate the path ending in -1
    path = []
    current_node = goal
    while current_node != -1:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]
    path.append(-1)
    
    return path

def print_shortest_path(path):
    if len(path) > 1 and path[0] != -1:
        # Print the path without the last -1
        print(" -> ".join(map(str, path[:-1])))
    else:
        print("No path found")

def main():
    if len(sys.argv) == 4:
        start = int(sys.argv[1])
        goal = int(sys.argv[2])
        filename = sys.argv[3]
        
        graph, num_rows, num_cols = read_txt_to_adjacency_matrix(filename)
        
        num_vertices = num_rows  # Assuming the number of vertices is the number of rows
        
        if start >= num_vertices or goal >= num_vertices:
            print(f"Error: Start ({start}) or goal ({goal}) node is out of bounds for graph with {num_vertices} nodes.")
            return
        
        previous_nodes = dijkstra(graph, num_vertices, start, goal)
        print_shortest_path(previous_nodes)
    else:
        print("Usage: python dijkstra.py <start> <goal> <filename>")

if __name__ == "__main__":
    main()