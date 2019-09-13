# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:10:53 2019

@author: rcato
"""
import numpy as np
import pylab as py
#import trianglePath

def main():
    #enter in the desired size of the triangle    
    size = 10
        
    theT = Triangle(size).triangleBuilder()
    
    for i in range(size):
        print(slabArray(theT, i)) 
    print('')
    
    print(BestPathFinder(theT, size).sumPath(), 'best path')
    

    

#first generate a random triangle
class Triangle:
    def __init__(self, size):
        self.size = size
        self.arrayOfPoints = []
    
    #now build a triangle with random points of size
    def triangleBuilder(self):
        
        #array to store points
        self.arrayOfPoints
        totalPoints = int(self.size * (self.size + 1) / 2)
        for i in range(totalPoints):
            self.arrayOfPoints.append(np.random.randint(0, 9))
        return self.arrayOfPoints

class BestPathFinder:
    def __init__ (self, fullTriangle, sizeOfT):
        self.fullTriangle = fullTriangle
        #smaller triangle to determine possible paths
        self.sizeOfT = int(sizeOfT)
    
    # total number of paths for the small triangle
    def totalNPaths(self):
        return 2**(self.sizeOfT - 1)
       
    # 0 = left turn, 1 = right turn
    # accessed by binaryMap()[attempt#][turn for node i]
    # i ranges from 0 to size of the triangle - 2, because the last nodes do 
    # not get to turn left or right.
    def binaryMap(self):
        choiceSize = self.sizeOfT - 1
        turnMap = []
        for i in range(self.totalNPaths()):
            binaryLR = bin(i)[2:].zfill(choiceSize)
            turnMap.append(binaryLR)
        
        return turnMap
         
    def sumPath(self):
        total = []
        paths = []
        #iterating over all but the last row
        for i in range(self.totalNPaths()):
            totali = self.fullTriangle[0]
            position = 0
            sizeRow = 0
            sizeNextRow = 1
            currentPath = [self.fullTriangle[0]]
            for j in range(self.sizeOfT - 1):
                sizeRow += 1
                sizeNextRow += 1
                # Order of turn doesn't matter, but we are turnning from the
                # top down
                turnDirection = int(self.binaryMap()[i][j])
                
                
                # Determining new position based off of left or right turn
                if turnDirection == 0:
                    #add the value of the current row
                    position += sizeRow
                    
                else:
                    position += sizeNextRow
                    
                #print(position, 'position before break')
                currentPath.append(self.fullTriangle[position])
                totali += self.fullTriangle[position]
            
            total.append(totali)
            paths.append(currentPath)
        
        bestPath = max(total)
        bestPathArray = []
        for i in range(self.totalNPaths()):
            if sum(paths[i]) == bestPath:
                if bestPathArray != []:
                    break
                bestPathArray = paths[i]
        
        for i in range(self.totalNPaths()):
            if paths[i] == bestPathArray:
                binArray = (self.binaryMap()[i])
                if len(binArray) != self.sizeOfT - 1:
                    tempString = '0'
                    for k in range(self.sizeOfT - 2 - len(binArray)):
                        tempString += '0'
                    tempString += binArray
                    binArray = tempString
                                
        return bestPath, bestPathArray, binArray

#for printing
def slabArray(triangle, row):
    rowLow  = int(row * (row+1) / 2)
    rowHigh = int((row + 1) * (row + 2) / 2)
    return triangle[rowLow : rowHigh]

                
main()            
            
            


      




