import random

'''
given a sorted array of integers and a target integer, return the index of the integer 
or -1 if target does not exist in the array. 
'''

def binary_search(arr, num):
    def __k(arr,l,r):
        m = int((r-l)/2)
        if arr[m] == num:
            return m
        elif l >= r:
            return -1
        elif arr[m] < num:
            l = m
            print (f'{arr[m]} < {num}')
            __k(arr, l, r)
        elif arr[m] > num:
            r = m
            print (f'{arr[m]} > {num}')
            __k(arr, l, r)
        else:
            return -1

    l,r = 0,len(arr)-1
    return __k(arr, l, r)


if __name__ == '__main__':
    arr01 = [-10, -5, -4, -1, 0, 2, 6, 8, 12, 22, 30]
    

    arrSize =  random.randint(0, 100)
    arrStart = random.randint(-500, 500)
    arrEnd = random.randint(-500, 500)

