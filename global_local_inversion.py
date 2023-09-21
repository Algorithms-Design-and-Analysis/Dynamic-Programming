# 775. Global and Local Inversions
# Medium
# 1.7K
# 361
# Companies
# You are given an integer array nums of length n which represents a permutation of all the integers in the range [0, n - 1].

# The number of global inversions is the number of the different pairs (i, j) where:

# 0 <= i < j < n
# nums[i] > nums[j]
# The number of local inversions is the number of indices i where:

# 0 <= i < n - 1
# nums[i] > nums[i + 1]
# Return true if the number of global inversions is equal to the number of local inversions.

 

# Example 1:

# Input: nums = [1,0,2]
# Output: true
# Explanation: There is 1 global inversion and 1 local inversion.
# Example 2:

# Input: nums = [1,2,0]
# Output: false
# Explanation: There are 2 global inversions and 1 local inversion.
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 0 <= nums[i] < n
# All the integers of nums are unique.
# nums is a permutation of all the numbers in the range [0, n - 1].

def mergeSort(array):

    ordenado = array
    if len(ordenado) > 1:
        #  r is the point where the ordenado is divided into two subordenados
        r = len(ordenado)//2
        L = ordenado[:r]
        M = ordenado[r:]
        # Sort the two halves
        mergeSort(L)
        mergeSort(M)
        i = j = k = 0
        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                ordenado[k] = L[i]
                i += 1
            else:
                ordenado[k] = M[j]
                j += 1
            k += 1
        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            ordenado[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            ordenado[k] = M[j]
            j += 1
            k += 1
    return ordenado

def interseccion(izquierda: list[int], derecha: list[int]):

    contador_locales = 1 if izquierda[len(izquierda)-1] > derecha[0]  else 0 
    
    izquierda_ordenado = mergeSort(izquierda)
    derecha_ordenado = mergeSort(derecha)
    
    izquierda_indice = 0
    derecha_indice = 0
    contador_globales = 0
    while izquierda_indice < len(izquierda_ordenado) and derecha_indice < len(derecha_ordenado):
        if izquierda_ordenado[izquierda_indice] > derecha_ordenado[derecha_indice]:
            contador_globales += abs(len(izquierda_ordenado) - izquierda_indice)
            derecha_indice += 1
        else:
            izquierda_indice += 1
    return contador_globales, contador_locales

def getGlobalesLocales(nums: list[int]) -> bool:
    if len(nums) == 1:
        return 0, 0
    elif len(nums) == 2:
        locales = 1 if nums[0] > nums[1] else 0
        globales = 1 if nums[0] > nums[1] else 0
        return globales, locales
    else:
        mitad = len(nums)//2
        izquierda = nums[:mitad]
        derecha = nums[mitad:]
        
        izquierda_globales, izquierda_locales = getGlobalesLocales(izquierda)
        derecha_globales, derecha_locales = getGlobalesLocales(derecha)
        interseccion_globales, interseccion_locales = interseccion(izquierda, derecha)
        nums_globales = izquierda_globales + interseccion_globales + derecha_globales
        nums_locales = izquierda_locales + interseccion_locales + derecha_locales
        return nums_globales, nums_locales
    
arreglo = []
archivo = open("./entrada.txt", 'r')
linea = archivo.readline()
while linea != '':
    linea = linea.replace("\n",  '')
    arreglo.append(int(linea))
    linea = archivo.readline()

print(getGlobalesLocales(arreglo)[0])