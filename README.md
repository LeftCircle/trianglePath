# trianglePath

TrianglePath uses a monte carlo solution to determine the best possible (largest) path when traversing down
a triangle generated with random integers. It begins with a greedy algorithm to determine a likely path, 
then randomly changes the path through thousands of iterations. This code works for any size triangle and is
extremely fast. 

# triangleBestPath

This solution determines the number of possible paths, and represents how each node is turned in binary. It 
then loops through all possible solutionsto determine the best route. Although it finds the correct route every
time, it does not scale as well with large triangles as my previous solution does. I attempted to mediate this
by breaking a large triangle into smaller ones and iterating through the large triangle by saving the best possible 
paths through the smaller triangles, but this would often generate incorrect answers and was not as fast or reliable
as the Monte Carlo method.
