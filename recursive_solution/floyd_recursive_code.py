#Floyd Warshall Algorithm using recursion

#We define INF as a large number. This is used
#to indicate that to vertices are not connected"""

INF = 9999

"""This function is a print function to display the solution 
on the screen using a nested loop"""

"""The outer loop has been coded using python's built in 
functionrange(). It iterates over the number of vertices 
that will be passed to the parameter numOfvertices. In this case 
the number will be 4 since there are 4 vertices"""

"""The inner loop will execute each vertices in the outer loop 
4 times, and if there is no path between the beginning vertices 
and the destination vertices, it will print INF. If there is, it 
will print the distance between each pair of vertices """

def printSolution(numOfVertices, distance):
    for i in range(numOfVertices):
        
        #It takes all vertices from the graph's columns (labeled as j)
        for j in range(numOfVertices):
            
            #If there is no direct path between two vertices it prints INF
            if(distance[i][j] == INF):
                print("INF", end=" ")
            
            #If there is a path between two vertices, it will print the distance
            else:
                print(distance[i][j], end="  ")
        print(" ")

"""This is the main recursive function. The function in this case will 
not only take the number of vertices (4) and the graph, but will also 
include a parameter (counter) to keep track of how many times is the function 
calling itself. When it reaches the beginning it will stop, if not, it will 
keep on calling itself"""

def floydWarshall2(numOfVertices, G, counter):
    distance = G

    #if counter===numOfVertices is the base case for the recursion. 
    #If the counter reaches the number of vertices, the function will stop
    if counter == numOfVertices:
      printSolution(numOfVertices, distance)    
    
      """for the else statement, the triple loop on the original iterative function 
      has been maintained, where the distances between i and j will be rewritten."""

      """The outer loop has been coded using python's built-in function range(). 
        The function range() iterates over the number of vertices that will be 
        passed to the parameter numOfvertices. In this case the number will be 4 since 
        there are 4 vertices"""
    else:
      
      #it takes all vertices one by one and sets them as intermediate vertices
      for k in range(numOfVertices):

        #It takes al vertices from the graph's rows (labeled as i)
        for i in range(numOfVertices):
          
          #It takes al vertices from the graph's columns (labeled as j)
          for j in range(numOfVertices):
            
            """if the distance between any two vertices using an intermediate 
            vertex is lesser that the direct distance between two vertices 
            without an intermediate vertex. The min() built in function returns 
            the distance with the lowest value"""
            distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
       
        
        """The last line on the function is where the recursion 
        is executed. Now that the distances have been rewritten 
        with the lowest distance value, the function calls itself 
        again. It maintains the same number of vertices but with 
        the changed distance parameters. The counter parameter keeps 
        track of how many times the function has been called. Every 
        time the function calls itself again, it will have done it once 
        more, hence it becomes we add +1 to the counter parameter"""   
      
      floydWarshall2(numOfVertices, distance, counter+1)

"""The floydwarshall2 function takes three parameters, so another 
function without the counter parameter needs to be created 
in order to get the output for the graph. floydwarshall calls 
Floydwarshall2 with the counter set to value 0"""
def floydWarshall (numOfVertices,G):
  floydWarshall2(numOfVertices, G, 0)

G = [[0, 7, INF, 8],
     [INF, 0, 5, INF],
     [INF, INF, 0, 2],
     [INF, INF, INF, 0]
     ]

"""It prints the result"""
floydWarshall(4, G)

#Using timeit to test the recursive code version performance
if __name__=="__main__":
  import timeit
  print("--------------")
  print(" ")
  print("Performance test using timeit:")
  print (timeit.timeit())
  

  