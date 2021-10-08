import numpy as np

#Create a 1D array of numbers from 0 to 9
a = np.arange(10)
print(a, "\n")


#Create a 3×3 NumPy array of all Boolean value Trues
array = np.ones((3, 3), dtype=bool)
print(array, "\n")


#Extract all odd numbers from array of 1-10
a = np.arange(1, 10, 2)
print(a, "\n")


#Replace all odd numbers in an array of 1-10 with the value -1
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
a[a % 2 == 1] = -1
print(a, "\n")


#Convert a 1D array to a 2D array with 2 rows
ar = np.arange(1, 7).reshape(2, -1)
print(ar, "\n")


#Create two arrays a and b, stack these two arrays vertically use the  np.dot and np.sum to calculate totals
a = np.arange(1, 17).reshape(4, 4)
b = np.arange(17, 33).reshape(4, 4)
c = np.dot(a, b)
sum = np.sum(c)

print(c, "\n")
print(sum,"\n")


# Extension: Create the following pattern without hardcoding. Use only NumPy  functions
a = np.array([1, 2, 3])
out = np.r_[np.repeat(a, 3), np.tile(a, 3)]
print(out, "\n")


#In two arrays a ( 1,2,3,4,5) and b ( 4,5,6,7,8,9) –remove all repeating  items present in array b
a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7, 8, 9])
c = np.intersect1d(a, b)
c1 = np.setdiff1d(a, b)

print(c)
print(c1,"\n")

#Get all items between 3 and 7 from a and b and sum them together
a = np.array([1, 2, 3, 4, 5])
var1 = a[(a >= 3) & (a <= 6)]
b = np.array([4, 5, 6, 7, 8, 9])
var2 = b[(b >= 3) & (b <= 6)]

c = np.dot(var1, var2)
sum = np.sum(c)
print(var1)
print(var2)

print(sum)
