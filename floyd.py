import math

def floyd_warshall(d, p):
    n = len(d)
    
    # initialize p with zeros
    for i in range(n):
        for j in range(n):
            p[i][j] = 0
    
    # iterate over all intermediate vertices
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # if the path through k is shorter than the direct path
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    p[i][j] = k + 1  # set the intermediate vertex on the path (add 1 to avoid 0 index)
                    
    return d, p

def main():
    # Example graph represented as an adjacency matrix
    graph = [
        [0, 3, math.inf, 7],
        [8, 0, 2, math.inf],
        [5, math.inf, 0, 1],
        [2, math.inf, math.inf, 0]
    ]
    
    # Initialize distance and path matrices
    n = len(graph)
    d = [row[:] for row in graph]  # make a copy of the graph
    p = [[0 for j in range(n)] for i in range(n)]
    
    # Compute shortest paths using Floyd-Warshall algorithm
    d, p = floyd_warshall(d, p)
    
    # Print results
    print("Distance matrix:")
    for row in d:
        print(row)
    
    print("\nPath matrix:")
    for row in p:
        print(row)
    
if __name__ == '__main__':
    main()

