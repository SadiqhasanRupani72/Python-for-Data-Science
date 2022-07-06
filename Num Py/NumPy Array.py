# firstly we will import numpy
import numpy as np

# Second we will create a list.
lst = [1, 2, 3, 4]

# then we will grab this list and store it into a array variable.

np_arr = np.array(lst);

# print displaying the array
print(f'\n The array list are given below.\n -> {np_arr}.\n ')

# Now we will create a matrix.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Then we will print the matrix.
print(f' Matrix: {matrix}.')

# This matrix variable is a normal python list.
# now if i convert this matrix var into a array then the numpy will detect that this var
# is a matrix, let's see!

matrix_arr = np.array(matrix)

print(f'\n The Matrix array list are given below.\n {matrix_arr}.\n')

# numpy arange() is just like a range func in python, it creates an array in the given range.
auto_create_arr = np.arange(0, 11)  # arange([start], [end], [jump_to])

print(f' Array created by using arange function in NumPy: {auto_create_arr}')

jump_to_arr = np.arange(0, 101, 2)  # [go from "num"],[up to but not including "num"],[jump_by "num"]

print(f'\n Arrays are: {jump_to_arr}.\n ')

np_zeros = np.zeros(5)  # If you pass a single number you will get one dimensional array.
'''
  Zeros(shape, dtype = float, order = 'C'
  
  It returns a new array of given shape and type, filled with zeros.
'''

print(f'\n One dimensional arrays of zeros array: {np_zeros}.\n')  # one dimensional array.

np_zeros = np.zeros((5, 6))  # This 2 numbers inside a tuple will get us a 2D array.

print(f'\n Two dimensional arrays of zeros: \n {np_zeros}')  # 2D arrays.

np_ones = np.ones((5,3))  # This will create a 2D array.
'''
  ones methods are the numpy's method,
  this returns a new array of given shapes and types, filled with ones 
  
  syntax:
    np.ones(shape, dtype = None, order='C') 
'''

print(f'\n 2D array of ones: \n {np_ones}')

np_eye = np.eye(5)  # five by five rows and columns.
print(f"\n The identity matrix is given below: \n {np_eye}")

one_d_rand = np.random.rand(5)
print(f"\n One dimensional array of random number between 0 to 1 elements are: \n {one_d_rand} \n")

two_d_rand = np.random.rand(5,2)  # Five cols and two rows.
print(f"\n Two dimnesional array of random number between 0 to 1 elements are: \n {two_d_rand} \n")

randn_array = np.random.randn(3)
print(f"\n randn arrays in 1-D array format: \n {randn_array}")

randn_array = np.random.randn(5,2)  # 5 by 2 array, no tuple, each dimension as a separate argument
print(f"\n randn arrays in 2-D array foramt: \n {randn_array}")

randint_array = np.random.randint(1,100)
print(f"\n randint in 1-D array format: \n {randint_array} \n")
# returns one random int, 1 inclusive, 100 exclusive.

randint_array = np.random.randint(1,100,10)
print(f"\n The 10 random integers between 1- 100 numbers in array format are given below. \n {randint_array}. ")

randint_array = np.random.randint(1,100,(5,2))
print(f"\n The 5 by 2 array of random integer between 1 - 100 numbers are given below. \n {randint_array}.")

random_seed = np.random.seed(56)
random_randint = np.random.randint(90, 100, 10)
print(f" \n Sample Output will generate: {random_randint}")
print(f" \n See! Same random numbers!!, by using random.seed: {random_randint}")

# let's create a arange array.
arange_arr = np.arange(0,26)
print(f'\n Arange arrays: {arange_arr}')

# reshaping the arange_arr variable in 2-D array.
reshaped_arr = arange_arr.reshape(13,2)

print(f'\n Reshaped arrays are: \n {reshaped_arr}.\n')

# creating a random arr
ranarr = np.random.randint(0,101,10)
# np.random.seed(0)
print(f"\n Random integers in array format from 0 to 100 is. \n -> {ranarr}")

# creating a variable will stores the maximum value of ranarr variable
max_arr = ranarr.max()
# we also can find the location of maximum value doing this,
loc = ranarr.argmax()
print(f"\n The maximum number from {ranarr} is \n -> {max_arr} \n and the location of this {max_arr} is in '{loc}th' index")


# creating a variable will stores the minimum value of ranarr variable
min_arr = ranarr.min()
# we also can find the location of minimum value doing this,
loc = ranarr.argmin()
print(f"\n The maximum number from {ranarr} is \n -> {min_arr} \n and the location of this {min_arr} is in '{loc}th' index")

data_type = ranarr.dtype
print(f"\n The data type of this {ranarr} array is '{data_type}'.")