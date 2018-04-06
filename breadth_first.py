#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:59:23 2017

@author: user
"""

while True:
    # n is number of nodes, and m is number of edges
    n, m = (raw_input().strip().split(' '))
    n,m = [int(n), int(m)]
    print 'in the outer loop with m=', m
    edgeList =[]
    while m > 0:
        print 'loop running'
        u,v = (raw_input().strip().split(' '))
        u,v = [int(u), int(v)]
        edgeList.append([u,v])
        print 'm = ', m
        m -= 1
#==============================================================================
#     adjacency matrix
#==============================================================================
    adj = [[0 for col in range(n)] for row in range(n)]


#==============================================================================
#   visited  & queue
#==============================================================================
    
    visited = [False for col in range(n)]
    visited[0] = True
    queue =[]
    def push(item):
        queue.append(item)
        print 'pushing item', item
        print 'queue is: ' , queue
        visited[item] = True

    def pop():
        
        popped = queue.pop(0)
        print 'popping: ', popped
        for node in range(len(adj[popped])):
            print 'node is', node
            print 'adj[popped][node] =', adj[popped][node]
            if adj[popped][node] == 1 and visited[node] == False:
                push(node)
                #print "pushing node:", node
        print 'queue:', queue
        print 'visited',visited
    def is_empty():
        if not queue:
            return True
        else:
            return False
#==============================================================================
#   populate adjacency matrix
#==============================================================================
    for edge in edgeList:
        print edge
        if adj[edge[0]][edge[1]] != 1:
              adj[edge[0]][edge[1]] = 1
        if adj[edge[1]][edge[0]] != 1: 
              adj[edge[1]][edge[0]] = 1  

    print edgeList
    for row in adj:
        print row
    
#==============================================================================
#   set starting node & queue it
#==============================================================================
    s = raw_input().strip()
    s = int(s)
    
    push(s)
#==============================================================================
#   pop starting node off queue and queue up connected nodes
#==============================================================================
    pop()
    pop()
    pop()