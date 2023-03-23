#!/usr/bin/env python
# -*- coding: utf-8 -*-

from linkedList import length, LinkedList, add, access

def exerciseOne(L):
    largo = length(L)
    currentNode = L.head
    menores = LinkedList()
    mayores = LinkedList()
    comparador = access(L, (largo/2) - 1)
    for i in range(0, largo):
        if comparador >= currentNode.value:
            if comparador != currentNode.value:
                add(menores, currentNode.value)
        else:
            add(mayores, currentNode.value)
        currentNode = currentNode.nextNode
        L.head = currentNode
    addList(L, mayores)
    add(L, comparador)
    addList(L, menores)
    
def addList(L, m):
    currentNode = m.head
    while currentNode != None:
        add(L, currentNode.value)
        currentNode = currentNode.nextNode
    

def contieneSuma(A,n):
    print(contieneSumaR(A.head, n))

def contieneSumaR(node, n):
    if node == None:
        return False
    aux = node.value
    nextNode = node.nextNode
    while node != None:
        if node.nextNode != None:
            if (aux + node.nextNode.value) == n:
                return True
        node = node.nextNode 
    return contieneSumaR(nextNode, n)

