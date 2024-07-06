#Q.1)WAP to create array elements between 25 to 45(20 elements).Arrange them in equal size array.

import numpy as np

#create an array by given start and end element
array = np.linspace(25,45,20)
print("original array",array)

reshape = array.reshape(2,10) #reshape it such that we will get 2 arrays with equal elements
print("reshaped array",reshape)



#Q.2)find array element greater than 10 

import numpy as np
array = np.array([2,15,2,12,5,66,44]) #create an array
print("array",array)
new_array = array[array>10] #applied required condition that is element is greater than 10
print("new array : ",new_array)


#Q.3)WAP to concatenate two array apply all mathematical operator on the same

import numpy as np
#create 2 separate arrays
arr1 = np.array([2,5,4])
arr2 = np.array([3,6,8])

#concatenate both arrays
arrnew = np.concatenate((arr1,arr2))
print(arrnew)

#mathematical operations
addition =np.add(arr1,arr2) #add both arrays
print("addition of both arrays:",addition)

subtract = np.subtract(arr1,arr2) #subtracted both arrays
print("subtraction of both arrays:",subtract)

multiply = np.multiply(arr1,arr2) #multiplied both arrays
print("multiplication of both arrays",multiply)

divide = np.divide(arr1,arr2) #divided both arrays
print("division of both arrays",divide)


#Q.4)Extract all odd numbers from array
import numpy as np
array = np.array([5,6,4,3,9,1]) #created an array
new_arr = array[array%2 != 0] #applied required condition in our new array to filter out the odd elements
print(new_arr)
