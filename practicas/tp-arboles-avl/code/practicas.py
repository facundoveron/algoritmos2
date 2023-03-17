class AVLTree:
	root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None

'''
Parte 1

Ejercicio 1
'''

def rotateLeft(B,node):
    currentNode = node.rightnode
    parent = node.parent

    node.rightnode = currentNode.leftnode
    currentNode.leftnode = node
    node.parent = currentNode

    if parent == None:
        B.root = currentNode
    else:
        currentNode.parent = parent
        if parent.leftnode == node:
            parent.leftnode = currentNode
        else:
            parent.rightnode = currentNode        

    return B


def rotateRight(B, node):
    currentNode = node.leftnode
    parent = node.parent

    node.leftnode = currentNode.rightnode
    currentNode.rightnode = node
    node.parent = currentNode

    if parent == None:
        B.root = currentNode
    else:
        currentNode.parent = parent
        if parent.leftnode == node:
            parent.leftnode = currentNode
        else:
            parent.rightnode = currentNode        

    return B


'''
    Ejercicio 2
'''

def calculateBalance(B):
    calculateBalanceR(B.root)    


def calculateBalanceR(node):
    if node == None:
        return
    else:
        leftHeight = heigthTree(node.leftnode) - 1
        rightHeight = heigthTree(node.rightnode) - 1
        node.bf = leftHeight - rightHeight

        if node.leftnode != None:
            calculateBalanceR(node.leftnode)
        if node.rightnode != None:
            calculateBalanceR(node.rightnode)

'''
    Ejercicio 3
'''

def reBalance(B):
    calculateBalance(B)
    rebalanceR(B,B.root)


def rebalanceR(B,node):
    if node.bf > 1 or node.bf < -1:
        if node.bf > 1 and node.leftnode.bf >= 0:
            rotateRight(B, node)
        else:
            if node.bf > 1 and node.leftnode.bf < 0:
                rotateRight(B,node)
                rotateLeft(B, node)
        
        if node.bf < -1 and node.rightnode.bf <= 0:
            rotateLeft(B, node)
        else:
            if node.bf < -1 and node.rightnode.bf > 0:
                rotateLeft(B, node)
                rotateRight(B, node)
    else:
        if node.leftnode != None:
            return rebalanceR(node.leftnode)
        if node.rightnode != None:
            return rebalanceR(node.rightnode)

    return B

'''
    Ejercicio 4
'''

def insert(B, element, key): 
    node = AVLNode()
    node.key = key
    node.value = element
    node.bf = 0
    if B.root == None:
        B.root = node
        return key
    newNode = insertR(B.root, node)
    update_bf(newNode.parent)
    nodo = searchBalance(newNode.parent)
    if nodo != None:
        rebalanceR(B, nodo)
    return newNode.key


def insertR(currentNode, node):
    a = None
    if currentNode.key > node.key:
        if currentNode.leftnode != None:
            a = insertR(currentNode.leftnode, node)
        else:
            node.parent = currentNode
            currentNode.leftnode = node
            return node
    else:
        if currentNode.rightnode != None:
            a = insertR(currentNode.rightnode, node)
        else:
            node.parent = currentNode
            currentNode.rightnode = node
            return node
    return a

def update_bf(node):
    if node == None:
        return
    else:
        leftHeight = heigthTree(node.leftnode) - 1
        rightHeight = heigthTree(node.rightnode) - 1
        node.bf = leftHeight - rightHeight
        update_bf(node.parent)         

def heigthTree(currentNode):
    return 0 if currentNode == None else 1 + max(heigthTree(currentNode.leftnode), heigthTree(currentNode.rightnode))    

def max(heigthLeftNode, heigthRightNode):
    return heigthLeftNode if heigthLeftNode > heigthRightNode else heigthRightNode


def searchBalance(node):
    if node == None:
        return
    else:
        if node.bf < -1 or node.bf > 1:
            return node
        else:
            return searchBalance(node.parent)

'''
    Ejercicio 5
'''

def delete(B,element):
    if B.root.value == element:
        if B.root.leftnode.rightnode != None:
            nodeReplace = B.root.leftnode.rightnode
            nodeReplace.leftnode = B.root.leftnode
            nodeReplace.rightnode = B.root.rightnode
            B.root = nodeReplace
        else:
            nodeReplace = B.root.rightnode.leftnode
            nodeReplace.leftnode = B.root.leftnode
            nodeReplace.rightnode = B.root.rightnode
            B.root = nodeReplace
    else:
        parent = deleteR(B.root,element)

    calculateBalance(B)
    nodo = searchBalance(parent)

    if nodo != None:
        rebalanceR(B, nodo) 

def deleteR(currentNode, element):
    a = None
    if currentNode.value == element:
        key = currentNode.key
        if currentNode.leftnode == None and currentNode.rightnode == None:
            nodo = currentNode
            currentNode = currentNode.parent
            nodo.parent = None
            if currentNode.leftnode.key == key:
                currentNode.leftnode = None
            else:
                currentNode.rightnode = None
            return currentNode
        elif (currentNode.leftnode != None and currentNode.rightnode == None) or (currentNode.rightnode != None and currentNode.leftnode == None):
            nodo = currentNode.leftnode if currentNode.leftnode else currentNode.rightnode
            currentNode = currentNode.parent
            if currentNode.leftnode.key == key:
                nodo.parent = currentNode
                currentNode.leftnode = nodo
            else:
                nodo.parent = currentNode
                currentNode.rightnode = nodo
            return currentNode
        else:
            nodoleft = currentNode.leftnode
            nodoright = currentNode.rightnode
            nodo = currentNode
            currentNode = currentNode.parent
            if nodoleft.leftnode == None and nodoleft.rightnode == None and nodoright.leftnode == None and nodoright.rightnode == None:
                nodoleft.parent = currentNode
                if currentNode.leftnode.key == key:
                    currentNode.leftnode = nodoleft
                else:
                    currentNode.rightnode = nodoleft
                nodoleft.rightnode = nodoright
            else:
                nodo_replace = nodoleft.rightnode if nodoleft.rightnode else nodoright.leftnode
                nodo_replace.parent = currentNode
                if currentNode.leftnode.key == key:
                    currentNode.leftnode = nodo_replace
                else:
                    currentNode.rightnode = nodo_replace
            return currentNode

    if currentNode.leftnode != None:
        a = deleteR(currentNode.leftnode, element)
    if currentNode.rightnode != None and a == None:
        a = deleteR(currentNode.rightnode, element)
    return a



def search(B, element):
    return searchR(B.root, element) if B.root is not None else None

def searchR(node, element):
    a = None
    if node.value == element:
        return node
    if node.leftnode != None:
        a = searchR(node.leftnode, element)
    if node.rightnode != None and a == None:
        a = searchR(node.rightnode, element)
    return a


strings = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d","e", "f"]
keys = [10, 6, 20, 8, 4, 13, 22,3,5,7,9,11,14,21,23]
bt = AVLTree()
for a in range(0, 15):
    insert(bt, strings[a], keys[a])
