import numpy as np

# See documentation for Numpy @ https://numpy.org/doc/stable/reference/module_structure.html

# 1 dimensional array
OneDimensionalArray = np.ndarray(shape= (1,3))
### print(OneDimensionalArray)
# This array prints a 1 x 3 matrix in the terminal (a single axis with a length of 3, we can express a line this way!)

### print(OneDimensionalArray.dtype) 
# A way to get the data types of the elements

# Here you can model a 3D system of X/Y/Z axes
sequence_of_sequence_of_sequence = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
### print(sequence_of_sequence_of_sequence)


# Some useful functions to automate creation of arrays with initialized elements
# An array of all zeros
all_zero_array = np.zeros((3,4))
### print(all_zero_array)
# An array of all ones
all_ones_array = np.ones((3,4))
###print(all_ones_array)

# arrange() function = like Python range function, but it returns an array (starting value, ending, increment)
arange_example = np.arange(10, 30, 5)
### print(arange_example) 

# Indexing/Slicing/Iterating
# 1D arrays can be manipulated like Python lists
# For 2D+ arrays, each axis has one index (denoted by a comma separated tuples)
