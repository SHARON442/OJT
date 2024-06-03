import numpy as np
#create an original array
original_array=np.array([1,2,3,4,5,6])
print ("original array: ", original_array)
#create the view of the array
view_array=original_array.view()
print("view of the original array is :",view_array)

view_array[2]=30
print('modified view of the array:',view_array)
print("original array after modifying the view :",original_array)

copy_array=original_array.copy()
print("copy array :",copy_array)

copy_array[0]=10
print("modified copy array:",copy_array)
print("original array after modifying the copy array:",original_array)