from decorators.function_timer import time_me
from memory_profiler import profile
import sys
import time
#https://www.codinginterview.com/netflix-interview-questions

@time_me
def test_timer():
    time.sleep(2)

def array_size():
    arr1 = []
    print (f'{sys.getsizeof(arr1)} bytes')
    for i in range(10):
        arr1.append('test')
        print(f'Array Length:\t{len(arr1)}')
        print (f'{sys.getsizeof(arr1)} bytes\n\n')

######################################################
#Given an array of integers and a value, 
#determine if there are any three integers in the array whose sum equals the given value.

def find_the_sum_of_two(A, val, start_index):
    #assumes sorted array
    i=start_index
    j= len(A)-1
    while i < j:
        s= A[i]+A[j]
        if s == val:
            return True
        if s < val: 
            i += 1
        else: 
            j -= 1
    return False
    
def find_sum_of_three(arr, require_sum): 
    arr.sort()
    for i in range(0, len(arr)-2):
        #start at the beginning of the array, how much do we have remaining to test?
        remainging_sum = require_sum - arr[i]
        #excluding i, are there any other 2 digital that add up to the remaining sum? 
        if find_the_sum_of_two(arr, remainging_sum, i+1):
            return True
    return False

###Runtime complexity
#Quadratic, O(n2)
###Memory complexity
#Constant, O(1)

#Given a two-dimensional array, if any element within is zero, make its whole row and column zero.
#assume an even matrix
def detect_zeros_in_matrix(matrix):
    rows=set()
    cols=set()
    for row_index in range(0, len(matrix)):
        [(rows.add(row_index), cols.add(col_index)) for col_index in range(0, len(matrix[row_index])) if matrix[row_index][col_index] == 0]

    return rows, cols
def set_zeros(rows, cols, matrix):
    for row_index in range(0, len(matrix)):
        if row_index in rows: 
            #set entire row to 0
            for col_index in range(0, len(matrix[row_index])):
                matrix[row_index][col_index] = 0
        else:
            for col_index in cols:
                matrix[row_index][col_index] = 0

    print (matrix)

if __name__ == '__main__':
#    a = [7,98,2,6,1,8,43]
#    print (find_sum_of_three(a, 56))

    matrix = [
            [1, 5, 45, 0, 81],
            [6, 7, 2, 82, 8],
            [20, 22, 49, 5, 5],
            [0, 23, 50, 4, 92],
        ]
    
    # matrix = [
    #     [5,4,3,9], 
    #     [2,0,7,6],
    #     [1,3,4,0],
    #     [9,8,3,4] 
    # ]
    rows, cols = detect_zeros_in_matrix(matrix)
    set_zeros(rows, cols, matrix)