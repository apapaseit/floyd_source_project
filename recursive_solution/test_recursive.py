import unittest
import floyd_recursive_code
from floyd_recursive_code import floydWarshall
from floyd_recursive_code import floydWarshall2
from floyd_recursive_code import printSolution
INF=9999

class RecursiveCodeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def test_floydWarshall2(self) -> None:
        distance=[[0, 7, INF, 8],
            [INF, 0, 5, INF],
             [INF, INF, 0, 2],
            [INF, INF, INF, 0]
     ]
        result=floyd_recursive_code.printSolution(4,distance)

        self.assertEqual(result, [[0, 7, 12, 8],
                                [INF, 0, 5, 7],
                                [INF, INF, 0, 2],
                                [INF, INF, INF, 0]
                             ])
        
        floydWarshall2(4, distance)
if __name__== "__main__":
    distance=[[0, 7, INF, 8],
            [INF, 0, 5, INF],
             [INF, INF, 0, 2],
            [INF, INF, INF, 0]
    ]
    unittest.main()
