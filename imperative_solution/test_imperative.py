from typing import List
import unittest
V = 4
INF = 99999


class Solution:
    def floydWarshall(self, graph):
        dist_tuples = list(map(tuple, graph))
        dist = [list(ele) for ele in dist_tuples]
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        self.printSolution(dist)
        return dist
    def printSolution(self, dist):
        print(
        )
        for i in range(V):
            for j in range(V):
                if dist[i][j] == INF:
                    print("{0}".format("INF"))
                else:
                    print("{0}\t".format(dist[i][j]))
                if j == V - 1:
                    print("")

#Unittest for imperative version
class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_floydWarshall(self) -> None:
        sol = Solution()
        graph = [
            [0, 5, INF, 10],
            [INF, 0, 3, INF],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0],
        ]
        self.assertEqual(
            [[0, 5, 8, 9], [INF, 0, 3, 4], [INF, INF, 0, 1], [INF, INF, INF, 0]],
            sol.floydWarshall(graph),
        )

if __name__ == "__main__":
    sol = Solution()
    graph = [[0, 5, INF, 10], [INF, 0, 3, INF], [INF, INF, 0, 1], [INF, INF, INF, 0]]
    # Print the solution
    sol.floydWarshall(graph)
    unittest.main()
    

