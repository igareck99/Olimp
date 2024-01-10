import csv
import string
import secrets

def insertionSort(l: list):
    for i in range(1, len(l)):
        temp = l[i]
        j = i - 1
        while (j >= 0 and temp[4] < l[j][4]):
            l[j + 1] = l[j]
            j = j - 1
        l[j + 1] = temp
    return list(reversed(l))
