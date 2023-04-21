from linkedList import LinkedList, Node, length, add
from algo1 import Array, input_int

'''
    Parte 1
'''

'''
    Ejercicio 1
'''

def insert(D, key, value):
    index = hash_multiplication(key, len(D))
    tuppla = (key,value)
    if D[index] == None:
        D[index] = LinkedList()
    addTupla(D[index], tuppla)

def search(D, key):
    index = hash(key, len(D))
    slot = D[index]
    if slot == None or slot.head == None:
        return
    else:
        node = slot.head
        while node != None:
            if node.value[0] == key:
                return key
            node = node.nextNode
        return

def delete(D, key):
    index = hash(key, len(D))
    slot = D[index]
    if slot == None or slot.head == None:
        return D
    else:
        node = slot.head
        if node == slot.head:
            slot.head = node.nextNode
            return D
        
        antNode = node
        node = node.nextNode
        while node != None:
            if node.value[0] == key:
                antNode.nextNode = node.nextNode
                return D
            antNode = node
            node = node.nextNode            
    return D

def hash(k, m):
    return k % m

def hash_multiplication(key, m):
    a=0.6180339887
    frac_part = key * a - int(key * a)
    return int(m * frac_part)


def addTupla(L, t):
    node = Node()
    node.value = t 
    if L.head == None:
        L.head = node
    else:
        nodo = L.head
        while nodo.nextNode != None:
            nodo = nodo.nextNode
        nodo.nextNode = node

'''
    Parte 2
'''

'''
    Ejercicio 3
'''

def exercise3():
    numberList = [61,62,63,64,65]
    D = Array(1000,LinkedList())
    for i in numberList:
        insert(D, i, i)
    


'''
    Ejercicio 4
'''

def permutations(S,P):
    weighing = 0
    weighing2 = 0
    for a,b in zip(S,P):
        weighing += ord(a)
        weighing2 += ord(b)

    return weighing == weighing2



'''
    Ejercicio 5
'''

def singleList(L):
    largo = length(L)
    D = Array(largo, LinkedList())
    node = L.head
    while node != None:
        insert(D, node.value, node.value)
        node = node.nextNode
        if node != None:
            if search(D, node.value) != None:
                return False
    return True


'''
    Ejercicio 6
'''

def hashCorreo(code, m):
    peso = ((ord(code[0]) * 1000) + ((ord(code[5]) * 100)) + ((ord(code[6]) * 10) + (ord(code[7]))))
    number = int(code[1:4])
    return (peso + number) % m


'''
    Ejercicio 7
'''

def compress(string):
    lyric = string[0]
    a = string[0]
    i = 0
    largo = len(string)
    j = 1
    cadena = ""
    while i <= largo:
        if i > 0:
            if a == lyric and i < largo:
                j += 1
            else:
                cadena += a
                if j > 1:
                    cadena += str(j)
                a = lyric
                j = 1
        i += 1
        if i < largo:
            lyric = string[i]
    return cadena

'''
    Ejercicio 8
'''

def idea(P, A):
    lengthLyric = len(P) - 1
    lengthString = len(A) - 1
    sentinel = lengthLyric
    D = Array(1,LinkedList()) 
    key = 0
    i = 0

    while lengthLyric >= 0:
        key += (ord(P[i]) - ord("a") + 1) * (10 ** lengthLyric)
        lengthLyric -= 1
        i += 1
    
    insert(D, key, P)

    string = ""
    i = 0
    key = 0
    lengthLyric = sentinel
    j = 0

    while j < lengthString:
        if i <= sentinel:
            key += (ord(A[j]) - ord("a") + 1) * (10 ** lengthLyric)
            string += A[j]
            lengthLyric -= 1
            i += 1
            j += 1
        else:
            if search(D, key) != None:
                return j - i
            string = ""
            key = 0
            i = 0
            lengthLyric = sentinel

    return -1

'''
    Ejercicio 9
'''

def subset(S,T):
    lenS = length(S)
    lenT = length(T)
    m = lenT + 1
    if lenS > lenT:
        return False

    D = Array(m, LinkedList())
    
    node = T.head
    while node != None:
        insert(D, node.value, node.value)
        node = node.nextNode

    node = S.head
    while node != None:
        if search(D, node.value) == None:
            return False
        node = node.nextNode

    return True

        
'''
    Ejercicio 10
'''
#h’(k) = k

def pollProbing():
    numberList = [10,22,31,4,15,28,17,88,59]
    D = Array(11, LinkedList())
    E = Array(11, LinkedList())
    F = Array(11, LinkedList())
    for i in numberList:
        hash_insert(D, i)
    print(D)

    for i in numberList:
        hash_insert2(E, i)
    print(E)

    for i in numberList:
        hash_insert3(F, i)
    print(F)

    print("fin")

def linearProbingHash(k, m, i):
    return (k + i) % m

def quadraticProbingHash(k, m, i):
    c1 = 1
    c2 = 3
    return (k + c1 * i + c2 * (i ** 2)) % m

def doubleHashing(k,m,i):
    h2 = 1 + (k % (m -1))
    return (k + i * h2) % m


def hash_insert(D, k):
    i = 0
    while i < len(D):
        j = linearProbingHash(k, len(D), i)
        if D[j] == None:
            D[j] = LinkedList()
            addTupla(D[j], k)
            break
        else:
            i += 1

def hash_insert2(D, k):
    i = 0
    while i < len(D):
        j = quadraticProbingHash(k, len(D), i)
        if D[j] == None:
            D[j] = LinkedList()
            addTupla(D[j], k)
            break
        else:
            i += 1

def hash_insert3(D, k):
    i = 0
    while i < len(D):
        j = doubleHashing(k, len(D), i)
        if D[j] == None:
            D[j] = LinkedList()
            addTupla(D[j], k)
            break
        else:
            i += 1

'''
    Ejercicio 12
'''

def testLinear():
    numberList = [12, 18, 13, 2, 3, 23, 5, 15]
    D = Array(10, LinkedList())
    for i in numberList:
        j = 1
        node = Node()
        node.value = i
        index = hash(i, 10)
        if D[index] == None:
            D[index] = LinkedList()
            D[index].head = node
        else:
            index += 1
            if D[index] == None:
                D[index] = LinkedList()
                D[index].head = node
            else:
                index += 1
                while D[index] != None:
                    index += 1
                D[index] = LinkedList()
                D[index].head = node


'''
    Ejercicio 13
'''

def testLinear():
    numberList = [46, 34, 42, 23, 52, 33]
    D = Array(10, LinkedList())
    for i in numberList:
        j = 1
        node = Node()
        node.value = i
        index = hash(i, 10)
        if D[index] == None:
            D[index] = LinkedList()
            D[index].head = node
        else:
            index += 1
            if D[index] == None:
                D[index] = LinkedList()
                D[index].head = node
            else:
                index += 1
                while D[index] != None:
                    index += 1
                D[index] = LinkedList()
                D[index].head = node
