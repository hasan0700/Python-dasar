from heapq import heappush, heappop

def dijkstra(graph, start):
    """
    Computes the shortest distance between the start node and all other nodes
    in the graph, using Dijkstra's algorithm.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_node = heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heappush(queue, (distance, neighbor))
    return distances

def shortest_distances(w, e, overpasses):
    """
    Computes the shortest distances between pairs of points on a grid, subject
    to some overpass connections.
    """
    western_stations = [(i+1, x) for i, x in enumerate(map(int, input().split()))]
    eastern_stations = [(j+1, f) for j, f in enumerate(map(int, input().split()))]
    graph = {}
    for i, x in western_stations:
        graph[i] = {}
        for j, f in eastern_stations:
            if f >= x:
                distance = f - x + 1
                graph[i][j] = distance
                graph[j][i] = distance
    for a, b in overpasses:
        graph[a][b] = 0
        graph[b][a] = 0
    shortest = []
    for i, x in western_stations:
        distances = dijkstra(graph, i)
        for j, f in eastern_stations:
            shortest.append(distances[j] + abs(f - x))
    shortest.sort()
    return shortest[:2]

t = int(input())
for case in range(1, t+1):
    w, e, c = map(int, input().split())
    overpasses = [tuple(map(int, input().split())) for _ in range(c)]
    distances = shortest_distances(w, e, overpasses)
    print("Case #{}: {:.10f} {:.10f}".format(case, distances[0], distances[1]))
