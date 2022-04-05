"""Implementations of some sorting"""
from inspect import ClosureVars
from os import close
import random


def merge(a0, a1, a):
    i = i0 = i1 = 0
    while(i != len(a)):
        if i0 == len(a0):
            a[i] = a1[i1]
            i1 = i1 + 1
        elif i1 == len(a1):
            a[i] = a0[i0]
            i0 = i0 + 1
        elif a0[i0] <= a1[i1]:
            a[i] = a0[i0]
            i0 = i0 + 1
        else:
            a[i] = a1[i1]
            i1 = i1 + 1
        i+= 1

def merge_sort(a):
    if len(a) <= 1:
        return a
    m = int(len(a)/2)
    a0 = merge_sort(a[0:m])
    a1 = merge_sort(a[m:len(a)])
    merge(a0,a1,a)
    return a


def _quick_sort(a, i, n):
    if n <= 1: 
        return

    x = a[i + random.randint(0,n-1)]
    (p,j,q) = (i-1, i, i + n)
    while j < q:
        if a[j]< x:
            p = p + 1
            a[j], a[p] = a[p], a[j]
            j = j + 1
        elif a[j] > x:
            q = q - 1
            a[j],a[q] = a[q], a[j]
        else:
            j = j + 1

    _quick_sort(a, i, p-i+1)
    _quick_sort(a, q , n - (q- i))

        
def quick_sort(a):
    _quick_sort(a, 0, len(a))
    return a
    

def binary_search(a, n, x):
    if len(a) == 0:
        return -1
    l = 0
    r = n - 1

    while r > l:
        mid = (l + r) // 2
        if x <= a[mid]:
            r = mid
        else:
            l = mid + 1
            
    if a[l] == x:
        return l
    num = a[l]
    if a[l] > x:
        if isinstance(num,int):
            return -1
        else:
            return l           

# print(binary_search([],0,0))
# print(binary_search([1,2,3,4,5], 5, 0))
# print(binary_search([1,2,3,4,5], 5, 1))

