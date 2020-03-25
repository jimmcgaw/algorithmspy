#!/usr/bin/env python


array = [5,4,1,8,7,2,6,3,89,9,10,1,2,41,7,3,32]


def merge(arrA, arrB):
    """ merge func for base case """
    result = []
    aIndex = 0
    bIndex = 0

    def appendFromA():
        nonlocal aIndex
        result.append(arrA[aIndex])
        aIndex += 1

    def appendFromB():
        nonlocal bIndex
        result.append(arrB[bIndex])
        bIndex += 1

    for i in range(len(arrA) + len(arrB)):

        if aIndex > len(arrA)-1:
            appendFromB()
        elif bIndex > len(arrB)-1:
            appendFromA()
        elif arrA[aIndex] > arrB[bIndex]:
            appendFromB()
        else:
            appendFromA()

    return result



def merge_sort(input_array):
    """ sort function for recursive case """
    if len(input_array) < 2:
        return input_array

    mid = len(input_array) // 2
    a, b = merge_sort(input_array[:mid]), merge_sort(input_array[mid:])

    return merge(a, b)
    

if __name__ == '__main__':
    print('input: {}'.format(array))
    print(merge_sort(array))