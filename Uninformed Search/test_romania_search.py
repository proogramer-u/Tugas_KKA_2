import unittest

from romania_search import bfs, build_map, dfs, ucs


class RomaniaSearchTests(unittest.TestCase):
    def test_all_searches_start_and_end_correctly(self):
        graph = build_map()

        for search in (dfs, bfs, ucs):
            path, distance = search(graph, "Arad", "Bucharest")
            self.assertEqual(path[0], "Arad")
            self.assertEqual(path[-1], "Bucharest")
            self.assertIsInstance(distance, int)

    def test_ucs_finds_shortest_distance(self):
        path, distance = ucs(build_map(), "Arad", "Bucharest")

        self.assertEqual(
            path,
            ["Arad", "Sibiu", "Rimnicu Vilcea", "Pitesti", "Bucharest"],
        )
        self.assertEqual(distance, 418)

    def test_search_reports_unreachable_goal(self):
        graph = {"Arad": [], "Bucharest": []}

        self.assertEqual(dfs(graph, "Arad", "Bucharest"), (None, None))
        self.assertEqual(bfs(graph, "Arad", "Bucharest"), (None, None))
        self.assertEqual(ucs(graph, "Arad", "Bucharest"), (None, None))

    def test_map_contains_reverse_roads(self):
        graph = build_map()

        for city, neighbours in graph.items():
            for other, distance in neighbours:
                self.assertIn((city, distance), graph[other])


if __name__ == "__main__":
    unittest.main()
