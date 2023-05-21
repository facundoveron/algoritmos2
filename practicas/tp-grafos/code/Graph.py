#!/usr/bin/env python
# -*- coding: utf-8 -*-

from algo1 import Array
from linkedList import LinkedList, length, add, Node, search, delete
from myqueue import enqueue, dequeue
import random

def createGraph(vertices, edges):
    n = length(vertices)
    if n <= 0:
        return
    graph = Array(n,LinkedList())
    node = vertices.head
    while node != None:
        nodo = Node()
        nodo.value = node.value
        index = hash(node.value, n)
        graph[index] = LinkedList()
        graph[index].head = nodo
        node = node.nextNode

    node = edges.head
    while node != None:
        addV(node.value[0], node.value[1], n, graph)
        addV(node.value[1], node.value[0], n, graph)
        node = node.nextNode

    return graph

def addV(v1, v2, n, graph):
    node = Node()
    node.value = v2
    index = hash(v1, n)
    edges = graph[index].head
    if edges.nextNode == None:
        edges.nextNode = node
    else:
        while edges != None:
            if edges.nextNode == None:
                edges.nextNode = node
                break
            edges = edges.nextNode


def hash(key, n):
    return (ord(key) - ord("a") + 1) % n

'''
    Ejercicio 2
'''

def existPath(graph, v1, v2):
    bfs(graph, v1)
    n = len(graph)
    vertex = graph[hash(v2, n)].head
    for i in range(n):
        if vertex.value[0] == v1:
            return True
        else:
            vertex = graph[hash(vertex.value[2], n)].head
    return False



def bfs(graph, s):
    for i in graph:
        value = i.head.value
        i.head.value = [value, "white",None,0]
    
    n = len(graph)
    vertex = graph[hash(s,n)].head
    vertex.value[1] = "grey"
    vertex.value[3] = 0
    Q = LinkedList()
    enqueue(Q,vertex)
    while Q.head != None:
        u = dequeue(Q)
        letter = u.value[0]
        colour = u.value[1]
        distance = u.value[3]
        while u != None:
            if colour == "white":
                vertex = graph[hash(u.value,n)].head
                vertex.value[1] = "grey"
                vertex.value[2] = letter
                vertex.value[3] = distance + 1
                enqueue(Q, vertex)
            u = u.nextNode
            if u != None:
                colour = graph[hash(u.value, n)].head.value[1]
        graph[hash(letter, n)].head.value[1] = "black"

'''
    Ejercicio 3
'''

def isConnected(graph):
    a = graph[0].head.value
    bfs(graph, a)
    for i in graph:
        if i.head.value[1] == "white":
            return False
    return True

'''
    Ejercicio 4
'''
def isTree(graph):
    return isConnected(graph) and cycleVerify(graph)
        

def cycleVerify(graph):
    s = graph[0].head.value
    for i in graph:
        value = i.head.value
        i.head.value = [value, "white",None]
    
    n = len(graph)
    vertex = graph[hash(s,n)].head
    vertex.value[1] = "grey"
    Q = LinkedList()
    enqueue(Q,vertex)
    while Q.head != None:
        u = dequeue(Q)
        letter = u.value[0]
        colour = u.value[1]
        if u.nextNode != None:
            node = u.nextNode
            while node != None:
                if graph[hash(node.value,n)].head.value[1] == "grey":
                    return False
                node = node.nextNode
        while u != None:
            if colour == "white":
                vertex = graph[hash(u.value,n)].head
                vertex.value[1] = "grey"
                vertex.value[2] = letter
                enqueue(Q, vertex)
            u = u.nextNode
            if u != None:
                colour = graph[hash(u.value, n)].head.value[1]
        graph[hash(letter, n)].head.value[1] = "black"
    return True    


'''
    Ejercicio 5
'''
def isComplete(graph):
    n = len(graph)
    j = 0
    for i in graph:
        node = i.head
        letter = i.head.value
        while node != None:
            j += 1
            node = node.nextNode
            if node != None:
                if node.value == letter:
                    return False
        if j == n:
            j = 0
        else: 
            return False
    return True

'''
    Ejercicio 6
'''
def convertTree(graph):
    s = graph[0].head.value
    for i in graph:
        value = i.head.value
        i.head.value = [value, "white",None]
    
    n = len(graph)
    vertex = graph[hash(s,n)].head
    vertex.value[1] = "grey"
    Q = LinkedList()
    edges = LinkedList()
    enqueue(Q,vertex)
    while Q.head != None:
        u = dequeue(Q)
        letter = u.value[0]
        colour = u.value[1]
        if u.nextNode != None:
            node = u.nextNode
            while node != None:
                if graph[hash(node.value,n)].head.value[1] == "grey":
                    nodo = Node()
                    nodo.value = [letter,node.value]
                    add(edges, nodo)
                node = node.nextNode
        while u != None:
            if colour == "white":
                vertex = graph[hash(u.value,n)].head
                vertex.value[1] = "grey"
                vertex.value[2] = letter
                enqueue(Q, vertex)
            u = u.nextNode
            if u != None:
                colour = graph[hash(u.value, n)].head.value[1]
        graph[hash(letter, n)].head.value[1] = "black"
    return edges

'''
    Parte 2
'''


def dfs(graph):
    for i in graph:
        value = i.head.value
        i.head.value = [value,"white",None,0,0]

    n = len(graph)
    time = 0
    for i in graph:
        if i.head.value[1] == "white":
            dfsR(graph, i.head, n, time)

def dfsR(graph,u,n, time):
    time += 1
    u.value[3] = time
    u.value[1] = "gray"
    letter = u.value[0]
    while u != None:
        vertex = graph[hash(u.value[0],n)].head
        if vertex.value[1] == "white":
            vertex.value[2] = letter
            dfsR(graph, vertex, n, time)
        u = u.nextNode
    
    if letter != None:
        g = graph[hash(letter,n)].head
        g.value[1] = "black"
        time += 1
        g.value[4] = time

'''
    Ejercicio 7
'''
def countConnections(graph):
    conexNumber = 0
    for i in graph:
        value = i.head.value
        i.head.value = [value,"white",None,0,0]

    n = len(graph)
    time = 0
    for i in graph:
        if i.head.value[1] == "white":
            conexNumber += 1
            dfsR(graph, i.head, n, time)

    return conexNumber
    

'''
    Ejercicio 8
'''
def convertToBFSTree(graph, v):
    for i in graph:
        value = i.head.value
        i.head.value = [value, "white",None]
    
    n = len(graph)
    vertex = graph[hash(v,n)].head
    vertex.value[1] = "grey"
    Q = LinkedList()
    enqueue(Q,vertex)
    j = 0
    graphReturn = Array(n, LinkedList())
    while Q.head != None:
        u = dequeue(Q)
        letter = u.value[0]
        colour = u.value[1]
        graphReturn[j] = LinkedList()
        node = Node()
        node.value = letter
        graphReturn[j].head = node
        node = graphReturn[j].head
        while u != None:
            if colour == "white":
                vertex = graph[hash(u.value,n)].head
                lyric = vertex.value[0] 
                vertex.value[1] = "grey"
                vertex.value[2] = letter
                nodoLyric = Node()
                nodoLyric.value = lyric
                node.nextNode = nodoLyric
                node = node.nextNode
                enqueue(Q, vertex)
            u = u.nextNode
            if u != None:
                colour = graph[hash(u.value, n)].head.value[1]
        j += 1
        graph[hash(letter, n)].head.value[1] = "black"

    return graphReturn
    
'''
    Ejercicio 9
'''
def convertToDFSTree(graph, v):
    for i in graph:
        value = i.head.value
        i.head.value = [value,"white",0]

    n = len(graph)
    vertex = graph[hash(v, n)].head
    colour = vertex.value[1]
    i = vertex
    j = 0
    while vertex != None:
        if colour == "white":
            convertToDFSTreeR(graph, i, n,j)
        vertex = vertex.nextNode
        if vertex != None:
            i = graph[hash(vertex.value,n)].head
            colour = i.value[1]

    graphR = Array(n, LinkedList())
    for i in graph:
        nodo = i.head
        position = nodo.value[2]
        graphR[position] = LinkedList()
        graphR[position].head = nodo

    return graphR

def convertToDFSTreeR(graph,u,n,j):
    u.value[1] = "gray"
    u.value[2] = j
    while u != None:
        vertex = graph[hash(u.value[0],n)].head
        if vertex.value[1] == "white":
            j += 1
            sentinel = convertToDFSTreeR(graph, vertex, n, j)
            if sentinel > j:
                j = sentinel
        u = u.nextNode
    return j

'''
    Ejercicio 10
'''

def bestRoad(graph, v1, v2):
    bfs(graph,v1)
    n = len(graph)
    edges = LinkedList()
    vertex = graph[hash(v2,n)].head    
    letter = vertex.value[2]
    while True:
        add(edges, (letter,vertex.value[0]))
        vertex = graph[hash(letter, n)].head
        if letter == v1:
            return edges
        letter = vertex.value[2]


'''
    Parte 3
'''


'''
    Ejercicio 14
'''

def prim(graph):
    n = len(graph)
    v = graph[0].head
    w = graph[0].head.nextNode
    visited = LinkedList()
    add(visited, v.value)
    Q = LinkedList()
    graphR = Array(n, LinkedList())
    j = 0
    for i in graph:
        graphR[j] = LinkedList() 
        node = Node()
        node.value = i.head.value
        graphR[j].head = node
        j += 1    

    while w != None:
        enqueue(Q, [(v.value,w.value),random.randint(1,9)])
        w = w.nextNode

    u = dequeue(Q)
    node = Node()
    node.value = (u[0][1],u[1])
    graphR[0].head.nextNode = node
    while u != None:
        w = u
        add(visited, w[0][1])
        r = graphR[hash(w[0][0],n)]
        if r.head.nextNode == None:
            node = Node()
            node.value = (w[0][1], w[1])
            r.head.nextNode = node
        elif r.head.nextNode.value[1] > u[1]:
            node = Node()
            node.value = (w[0][1],w[1])
            r.head.nextNode = node   
        v = graph[hash(w[0][1],n)].head
        w = graph[hash(w[0][1],n)].head.nextNode
        while w != None:
            if search(visited, w.value) == None:
                enqueue(Q, [(v.value,w.value), random.randint(1,9)])
            w = w.nextNode
        u = dequeue(Q)
    return graphR 


'''
    Ejercicio 15
'''
def kruskal(graph):
    n = len(graph)
    sets = Array(n,("",""))
    j = 0
    A = LinkedList()
    B = LinkedList()
    for i in  graph:
        add(A,(i.head.value))
        sets[j] = (i.head.value, i.head.value)
        j += 1
    edges = LinkedList()
    sortEdges(graph, edges)
    nodo = edges.head
    while nodo != None:
        if find(sets,nodo.value[0],n) != find(sets, nodo.value[1],n):
            add(B,((nodo.value[0], nodo.value[1])))
            union(sets, nodo.value[0], nodo.value[1], n)
        nodo = nodo.nextNode
    return createGraph(A,B)

def sortEdges(graph, edges):
    visited = LinkedList()
    for i in graph:
        nodo = i.head
        vertex = nodo.value
        nodo = nodo.nextNode
        while nodo != None:
            if search(visited, nodo.value[0]) == None:
                enqueuePriority(edges, (vertex, nodo.value[0], nodo.value[1]))
            nodo = nodo.nextNode
        add(visited, vertex)

def union(sets, u, v, n):
    newGroup = find(sets, u, n)
    otherGroup = find(sets, v, n)
    sets[hash(otherGroup,n)] = (otherGroup,newGroup)

def find(sets,vertex,n):
    if sets[hash(vertex, n)][1] == vertex:
        return vertex

    group = find(sets, sets[hash(vertex,n)][1], n)
    sets[hash(vertex,n)] = (vertex,group)
    return group


def enqueuePriority(Q, value):
    node = Node() 
    node.value = value
    head = Q.head
    flag = True
    if head == None:
        Q.head = node
    else:
        pre = head
        while head != None:
            if head.value[2] > node.value[2]:
                if head.value == Q.head.value:
                    node.nextNode = Q.head
                    Q.head = node
                else:   
                    nodo = pre.nextNode
                    pre.nextNode = node
                    node.nextNode = nodo
                flag = False
                break
            pre = head
            head = head.nextNode
        if flag:
            pre.nextNode = node

'''
    Parte 4
'''


'''
    Ejercicio 21
'''

def dijkstra(graph,s,v):
    n = len(graph)
    initRelax(graph, s)
    S = LinkedList()
    Q = LinkedList()
    enqueue(Q, graph[hash(s, n)].head)
    while Q != None:
        nodo = dequeue(Q)
        u = nodo
        add(S, u.value[0])
        nodo = nodo.nextNode
        while nodo != None:
            if search(S, nodo.value[0]) == None:
                v = graph[hash(nodo.value[0],n)]
                w = nodo.value[1]
                relax(u.value, v.head.value, w, Q, graph)
            nodo = nodo.nextNode

def minQueue(graph, Q):
    for i in graph:
        if i.head.value[1] != None:
            nodo = Node()
            nodo.value = i.head
            if Q.head == None:
                Q.head = nodo
                break

def initRelax(graph,s):
    n = len(graph)
    for i in graph:
        letter = i.head.value
        i.head.value = [letter, None, None]
    graph[hash(s,n)].head.value[1] = 0

def relax(u,v, w, Q, graph):
    if v[1] == None or v[1] > (u[1] + w):
        v[1] = u[1] + w
        v[2] = u[0]
        enqueue(Q, graph[hash(v[0],5)].head)
        