#First, let's create an array of even integers from 30 to 70:
import numpy as np

# Create array of even integers from 30 to 70
even_array = np.arange(30, 71, 2)
print("Array of even integers from 30 to 70:")
print(even_array)

# Generate 15 random numbers from standard normal distribution
normal_array = np.random.standard_normal(15)
print("\
Array of 15 random numbers from standard normal distribution:")
print(normal_array)

# Create two matrices for cross product
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Compute cross product
cross_product = np.cross(matrix1, matrix2)
print("\
Cross product of matrices:")
print(cross_product)

# Compute determinant of matrix1
det = np.linalg.det(matrix1)
print("\
Determinant of first matrix:")
print(det)

# Create a 3x3 array with random values
random_3x3 = np.random.rand(3, 3)
print("\
3x3 array with random values:")
print(random_3x3)

# Create a 5x5 array with random values
random_5x5 = np.random.rand(5, 5)

# Find the minimum and maximum values in the 5x5 array
min_value = np.min(random_5x5)
max_value = np.max(random_5x5)
print("\
5x5 array with random values:")
print(random_5x5)
print("\
Minimum value in 5x5 array:", min_value)
print("Maximum value in 5x5 array:", max_value)


# Create a sample array
sample_array = np.random.rand(4, 3)

# Compute mean, standard deviation, and variance along second axis
mean = np.mean(sample_array, axis=1)
std = np.std(sample_array, axis=1)
var = np.var(sample_array, axis=1)

print("\
Sample array:")
print(sample_array)
print("\
Mean along second axis:", mean)
print("Standard deviation along second axis:", std)
print("Variance along second axis:", var)
