
# as i can be anything less than x+1 so we will loop till x+1, than j till y+1, and k till z+1
# also ensuring i+j+k is not equal to n

x = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(x)


# In loop
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if i+j+k !=n:
#                 print(i,j,k)