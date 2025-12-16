import numpy as np

# Question 1
arr1 = np.arange(5, 26)
print(arr1)
arr2 = np.random.randint(10, 51, (3, 4))
print(arr2)

# Question 2
print(arr1.shape)
print(arr1.size)
print(arr1.dtype)
print(arr2.shape)
print(arr2.size)
print(arr2.dtype)

# Question 3
array1 = np.array([2, 4, 6, 8, 10])
array2 = np.array([1, 3, 5, 7, 9])
print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)

# Question 4
arr_2d = np.arange(1, 10).reshape(3, 3)
print(arr_2d)
broadcasted = arr_2d * 5
print(broadcasted)

# Question 5
arr5 = np.arange(10, 26).reshape(4, 4)
print(arr5[1])
print(arr5[:, -1])
arr5[0] = 0
print(arr5)

# Question 6
arr6 = np.random.randint(20, 41, 10)
print(arr6)
print(arr6[arr6 > 30])

# Question 7
arr7 = np.arange(11, 23)
reshaped7 = arr7.reshape(3, 4)
print(reshaped7)

# Question 8
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A @ B)
print(A.T)

# Question 9
arr9 = np.random.randint(10, 61, 15)
print(arr9.mean())
print(np.median(arr9))
print(arr9.std())

# Question 10
A10 = np.array([[2, 1, 3], [0, 5, 6], [7, 8, 9]])
print(np.linalg.det(A10))
print(np.linalg.inv(A10))
print(np.linalg.eig(A10))

# Question 11
positions = np.array([[0, 0], [2, 3], [4, 7], [7, 10], [10, 15]])
print(np.linalg.norm(positions[-1] - positions[0]))
step_distances = np.linalg.norm(np.diff(positions, axis=0), axis=1)
print(step_distances.sum())




