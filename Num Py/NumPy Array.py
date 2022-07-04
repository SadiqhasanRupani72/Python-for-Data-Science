# firstly we will import numpy
import numpy as np

# Second we will create a list.
lst = [1,2,3,4]

# then we will grab this list and store it into a array variable.

np_arr = np.array(lst);

# print displaying the array
print(f'\n The array list are given below.\n -> {np_arr}.\n ')

# Now we will create a matrix.
matrix = [[1,2,3],[4,5,6],[7,8,9]]

# Then we will print the matrix.
print(f' Matrix: {matrix}.')

# This matrix variable is a normal python list.
# now if i convert this matrix var into a array then the numpy will detect that this var
# is a matrix, let's see!

matrix_arr = np.array(matrix)

print(f'\n The Matrix array list are given below.\n {matrix_arr}.\n')

#numpy arange() is just like a range func in python, it creates an array in the given range.
auto_create_arr = np.arange(0,11) # arange([start], [end], [jump_to])

print(f' Array created by using arange function in NumPy: {auto_create_arr}')

jump_to_arr = np.arange(0,101,2) # [go from "num"],[up to but not including "num"],[jump_by "num"]

print(f'\n Arrays are: {jump_to_arr}.\n ')