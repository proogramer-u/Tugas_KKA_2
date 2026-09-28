from collections import deque
import heapq
from itertools import count


def build_map():
    """Return the undirected Romania road map from the assignment image."""
    graph = {}

    roads = [
        ("Arad", "Zerind", 75),
        ("Arad", "Sibiu", 140),
        ("Arad", "Timisoara", 118),
        ("Zerind", "Oradea", 71),
        ("Oradea", "Sibiu", 151),
        ("Sibiu", "Fagaras", 99),
        ("Sibiu", "Rimnicu Vilcea", 80),
        ("Timisoara", "Lugoj", 111),
        ("Lugoj", "Mehadia", 70),
        ("Mehadia", "Drobeta", 75),
        ("Drobeta", "Craiova", 120),
        ("Craiova", "Rimnicu Vilcea", 146),
        ("Craiova", "Pitesti", 138),
        ("Rimnicu Vilcea", "Pitesti", 97),
        ("Pitesti", "Bucharest", 101),
        ("Fagaras", "Bucharest", 211),
        ("Bucharest", "Giurgiu", 90),
        ("Bucharest", "Urziceni", 85),
        ("Urziceni", "Vaslui", 142),
        ("Vaslui", "Iasi", 92),
        ("Iasi", "Neamt", 87),
        ("Urziceni", "Hirsova", 98),
        ("Hirsova", "Eforie", 86),
    ]

    for city, neighbour, distance in roads:
        graph.setdefault(city, []).append((neighbour, distance))
        graph.setdefault(neighbour, []).append((city, distance))

    return graph


def dfs(graph, start, goal):
    """Mencari rute dengan pencarian DFS."""
    stack = [(start, [start], 0)]
    visited = set()

    while stack:
        city, path, distance = stack.pop()
        if city in visited:
            continue
        visited.add(city)

        if city == goal:
            return path, distance

        for neighbour, road_distance in reversed(graph.get(city, [])):
            if neighbour not in visited:
                stack.append(
                    (neighbour, path + [neighbour], distance + road_distance)
                )

    return None, None


def bfs(graph, start, goal):
    """Mencari rute dengan pencarian BFS."""
    queue = deque([(start, [start], 0)])
    visited = {start}

    while queue:
        city, path, distance = queue.popleft()
        if city == goal:
            return path, distance

        for neighbour, road_distance in graph.get(city, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(
                    (neighbour, path + [neighbour], distance + road_distance)
                )

    return None, None


def ucs(graph, start, goal):
    """Mencari rute dengan total jarak terpendek."""
    sequence = count()
    queue = [(0, next(sequence), start, [start])]
    best_distance = {start: 0}

    while queue:
        distance, _, city, path = heapq.heappop(queue)
        if distance != best_distance.get(city):
            continue

        if city == goal:
            return path, distance

        for neighbour, road_distance in graph.get(city, []):
            new_distance = distance + road_distance
            if new_distance < best_distance.get(neighbour, float("inf")):
                best_distance[neighbour] = new_distance
                heapq.heappush(
                    queue,
                    (new_distance, next(sequence), neighbour, path + [neighbour]),
                )

    return None, None


def print_result(name, result):
    path, distance = result
    print(f"{name}:")
    if path is None:
        print("  Tidak ada rute")
    else:
        print(f"  Rute: {' -> '.join(path)}")
        print(f"  Jarak: {distance} km")


def main():
    graph = build_map()
    start = "Arad"
    goal = "Bucharest"

    print(f"Pencarian rute dari {start} ke {goal}\n")
    print_result("DFS", dfs(graph, start, goal))
    print_result("BFS", bfs(graph, start, goal))
    print_result("UCS", ucs(graph, start, goal))


if __name__ == "__main__":
    main()
