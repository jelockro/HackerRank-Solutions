#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:50:55 2017

@author: user
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import numpy as np

#queries
q = input()



while q > 0:
    n, m = (raw_input().strip().split(' '))
    n,m = [int(n), int(m)]
    print 'in the outer loop with m=', m
    vertexList =[]
    while m > 0:
        print 'loop running'
        u,v = (raw_input().strip().split(' '))
        u,v = [int(u), int(v)]
        vertexList.append([u,v])
        print 'm = ', m
        m -= 1
#==============================================================================
# find highest value in vertextList
#==============================================================================
    highestNode = 0
    
    for vertex in vertexList:
        for node in vertex:
            if node > highestNode:
                highestNode = node
    
#==============================================================================
# initialize list of highestNode + 1 
# so each node is indexed at its own number
# make each entry false
#==============================================================================

    nodeList= []
    for i in range(highestNode + 1):
        nodeList.append([False, -1])


#==============================================================================
# start populating nodeList with associated nodes from vertexList
#==============================================================================



    for entry in vertexList:
        if not nodeList[entry[0]][0]:
            nodeList[entry[0]][0]= [entry[1]]
        
        if not nodeList[entry[1]][0]:
            nodeList[entry[1]][0]= [entry[0]]
        
        if entry[1] not in nodeList[entry[0]][0]:
            nodeList[entry[0]][0].append(entry[1])
        
        if entry[0] not in nodeList[entry[1]][0]:
            nodeList[entry[1]][0].append(entry[0])
        m =- m
    print vertexList
    print nodeList
##establish starting node
    s = raw_input().strip()
    s = int(s)
    nodeList[s][1] = 0
    edgeLength = 6
    
    for node in nodeList[s][0]:
        nodeList[node][1] = 1
    
    print nodeList

#iterates the lists in a list of lists
    for entry in nodeList:
        if entry[0] and entry[1] < 0:
            for node in entry[0]:
                if nodeList[node][1] > 0:
                    entry[1] = nodeList[node][1] + 1
    print nodeList
    
    for entry in nodeList:
        if entry[1] > 0:
            print entry[1] * edgeLength
        elif entry[1] < 0:
            print entry[1]

#def nodeSearch(dict):
#    #key loop
#
#    for key in dict:
#        #print '\n'
#        
#        nodeCount = 0  #if < 1 there are no starting nodes
#        #print 'initialized node count:', nodeCount
#        
#        
#        keysNotToStart= []
#
#        #run listSearch function
#        countDict[key] = listSearch(key)
#        
#    #print ' \n \n Keys that didn\'t connect to start:', searchDict
#    #print ' \n The current counts:', countDict
#
#
#
#
##print d
#nodeSearch(d)
#for key in countDict:
#    sys.stdout.write(str(countDict[key]),)
#for i in range(n - len(countDict)):
#    sys.stdout.write('-1',)
#
