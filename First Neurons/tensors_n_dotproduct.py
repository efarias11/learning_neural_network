# tensors are similar to arrays and matricies but have subtle differences (are setup as a list)
# a tensor object is an object that can be represented as an array
# they aren't exactly arrays be we are going to represent them as one
# a homologous container have to be uniform is structure and data type (no ragged arrays)

# the 3D array shape is (3,2,4)
# lolol = [[[1,5,6,2], # the outer array contains 3 elements, each inner matrix contains 2 lists or 2 rows, and 4 columns
#           [3,2,1,3]],
         
#          [[5,2,1,2],
#           [6,4,8,4]],
          
#          [[2,8,5,3],
#           [1,1,9,4]]]

# we use the numpy dot product to multiply vector and matricies which results in a scalar (a single # value)
# we could use a cross product which results in a vector

a = [1, 2, 3]
b = [2, 3, 4]

dot_product = a[0]*b[0]+ a[1]*b[1]+ a[2]*b[2]
print(dot_product)