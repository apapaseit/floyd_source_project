This README outlines a comparison between an iterative and a recursive implementation of the Floyd Warshall algorithm in Python by - Alfredo Papaseit.

Introduction

We have been presented with a simple iterative implementation of the Floyd Warshall Algorithm for a given weighted graph with 4x4 vertices (nodes) and edges with values associated representing a distance matrix among the nodes. Rows are labeled as i and columns as j and represent the vertices of the graph. Each cell in the graph represents the distance between each pair of vertices. If there is no value associated with that path, we have represented it as INF. The distance (D) from a vertex to itself is 0.

We need to find the shortest path between all pairs of paths, with the possibility of using an intermediate vertex (k). Hence, We will check paths from i to j using one vertex at a time (0 to 3) as an intermediate vertex. Following Floyd Warshall’s algorithm, (D[i][k] + D[k][j]) if (A[i][j] > A[i][k] + A[k][j]  every time  the distance between a pair of nodes through an intermediate vertix is lesser than the direct distance between the same two nodes, we will replace the value in the matrix for the smaller value.
