#num py 
#large dataset 
#list 

temperatur = [34.5,33.4,32.1,35.3,33.7]     #list
total=0
for temp in temperatur:
    total +=temp

avg=total/len(temperatur)    
print(avg)

#-------------------------------------------------

import numpy as np 

# arr_np = np.array([34.5,33.4,32.1,35.3,33.7])
# print(arr_np)

# print(arr_np.dtype)

# arr_np2=np.array([1,2,3,4,5,6,7])
# print(arr_np2.dtype)


# avg_temp=np.mean(temperatur)
# print(avg_temp)

# #----------------------------------------------------
# # r c
# # [1,2,3]
# # 
# # [[1,2,3]
# # [4,5,6]
# # [7,8,9] ]

# np_z = np.zeros(5)    #float
# print(np_z)

# np_z = np.zeros((2,3))    #float
# print(np_z)

# np_z = np.zeros(3,dtype=int)    
# print(np_z)

# np_z = np.zeros((2,3),dtype=int)    
# print(np_z)

# np_o=np.ones(5)
# print(np_o)

# np_o=np.ones(5)
# print(np_o)

