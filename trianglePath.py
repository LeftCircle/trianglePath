# largest triangle path
"""
Created on Tue Aug 27 09:19:53 2019
This is a quick program to determine the largest path down a size 5 triangle.
To have a robust method able to deal with size n triangles, monte carlo 
could be used to determine what is likely to be the best path
@author: rcato
"""
import numpy as np

#first generate a random triangle
class Triangle:
    def __init__(self, size):
        self.size = size
    
    #now build a triangle with random points of size
    def triangleBuilder(self):
        
        #array to store points
        arrayOfPoints = []
        totalPoints = int(size * (size + 1) / 2)
        for i in range(totalPoints):
            arrayOfPoints.append(np.random.randint(0, 9))
        
        return arrayOfPoints


#triangle must first be built for the below functions
#awful print function because I don't really want to optimize it
def printTriangle(size, triangle):
    totalPoints = int(size * (size + 1) / 2)
    
    for i in range(totalPoints):
        print(triangle[i])

#indexed at 0
def slabArray(triangle, row):
    rowLow  = int(row * (row+1) / 2)
    rowHigh = int((row + 1) * (row + 2) / 2 - 1)
    return triangle[rowLow : rowHigh]

def comparePoints(i, j):
    if i > j:
        return i
    if i < j:
        return j
    else:
        chance = np.random.randint(1, 10)
        if chance < 5:
            return i
        else:
            return j

def comparePointsMC(i, j, iteration):
    if np.random.random() > 0.9 + 1 / iteration:
        if i > j:
            return j
        if i < j:
            return i
        else:
            chance = np.random.randint(1, 10)
            if chance < 5:
                return i
            else:
                return j
    else:
        return comparePoints(i, j)

#returns the largest sum of the path moving from top to bottom by going
#through adjacent numbers
#
def largestPathGreedy(size, triangle):
    greedyPath = []
    # pick the first one
    greedyPath.append(triangle[0])
    
    #pick the second
    greedyPath.append(comparePoints(triangle[1], triangle[2]))
    for i in range(size - 2):
        #now check current position and position + 1 of the line below
        #checking the index in the triangle array
        currentIndex = theT.index(greedyPath[i + 1])
         
        #determining where on the current line this is
        currentPos = currentIndex - int((i + 1) * (i + 2) / 2)
        print(int((i + 1) * (i + 2) / 2), 'i -', 
              currentIndex, 'cI =', currentPos, 'cp')
        
        nextLineStart = int((i + 2) * (i + 3) / 2)
        
        #comparing adjacent values in the next line
        nPointL = nextLineStart + currentPos
        nPointR = nPointL + 1
        
        greedyPath.append(comparePoints(triangle[nPointL], triangle[nPointR]))
        print(comparePoints(triangle[nPointL], triangle[nPointR]), 'compp')
    print(greedyPath)
    return(sum(greedyPath))

def mCPath(size, triangle, iterations):
    
    tempPathSum = largestPathGreedy(size, triangle)
    #pick the second
    for j in range(iterations):
        mcPath = []
        mcPath.append(triangle[0])
        mcPath.append(comparePointsMC(triangle[1], triangle[2], j))
        for i in range(size - 2):
            #now check current position and position + 1 of the line below
            #checking the index in the triangle array
            currentIndex = theT.index(mcPath[i + 1])
             
            #determining where on the current line this is
            currentPos = int((i + 1) * (i + 2) / 2) - currentIndex
            
            nextLineStart = int((i + 2) * (i + 3) / 2)
            
            #comparing adjacent values in the next line
            nPointL = nextLineStart + currentPos
            nPointR = nPointL + 1
            
            mcPath.append(comparePointsMC(triangle[nPointL],
                                          triangle[nPointR], j))
        mcPathSum = sum(mcPath)
        if mcPathSum > tempPathSum:
            tempPathSum = mcPathSum
    return tempPathSum
    
    
    
    
    
    
size = 4
theT = Triangle(size).triangleBuilder()
printTriangle(size, theT)
lg = largestPathGreedy(size, theT)
print(lg)
#print(mCPath(size, theT, 100), 'mc', lg, 'greedy')                

