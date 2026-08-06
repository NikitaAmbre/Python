# '''
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# '''


# n=int(input('Enter value for rows and columns: '))
# for i in range(1,n+1): #outer loop for rows
#   for j in range(1,n+1): #inner loop for columns
#     print('*',end=' ')
#   print() #after completion of the inner loop to take the control in next line


# #Primary diagonal

# n=int(input('Enter a value: '))

# for i in range(1,n+1): #rows
#   for j in range(1,n+1):
#     if i==j:
#       print('*',end=' ')
#     else:
#       print(' ',end=' ')
#   print()

# #lower triangle w.r.t. primary diagonal

# n=int(input('Enter a value: '))

# for i in range(1,n+1): #rows
#   for j in range(1,n+1): #columns
#     if i>=j:
#       print('*',end=' ')
#     else:
#       print(' ',end=' ')
#   print()

# # #upper triangle w.r.t. primary diagonal

# n=int(input('Enter a value: '))

# for i in range(1,n+1): #rows
#   for j in range(1,n+1): #columns
#     if i<=j:
#       print('*',end=' ')
#     else:
#       print(' ',end=' ')
#   print()

# #secodary diagonal

# n=int(input('Enter a value: '))

# for i in range(1,n+1): #rows
#     for j in range(1,n+1):
#         if i+j==n+1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# # #lower triangle w.r.t. secndary diagonal
# n=int(input('Enter a value: '))

# for i in range(1,n+1): #rows
#     for j in range(1,n+1):
#         if i+j>=n+1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# # #upper triangle w.r.t. secondary diagonal

# n=int(input('Enter a value: '))

# for i in range(1,n+1): #rows
#     for j in range(1,n+1):
#         if i+j<=n+1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# '''
# @
# * @
# * * @
# * * * @
# * * * * @
# '''
# n=int(input('Enter a value: '))

# for i in range(1,n+1): #rows
#   for j in range(1,n+1): #columns
#     if i==j:
#       print('@',end=' ')
#     elif i>j:
#       print('*',end=' ')
#     else:
#       print(' ',end=' ')
#   print()


# # #print the pattern of hollow square

# n=int(input('Enter a value:'))

# for i in range(1,n+1):
#   for j in range(1,n+1):
#     if j==1 or i==1 or i==n or j==n:
#       print('*',end=' ')
#     else:
#       print(' ',end=' ')
#   print()


# #print the pattern +.

# n=int(input('Enter a value:'))

# for i in range(1,n+1): #rows
#   for j in range(1,n+1): #columns
#     if i==n//2+1 or j==n//2+1:
#       print('*',end=' ')
#     else:
#       print(' ',end=' ')
#   print()

# #Print the pattern X.

# n=int(input('Enter a value:'))

# for i in range(1,n+1): #rows
#   for j in range(1,n+1): #columns
#     if i==j or i+j==n+1 :
#       print('*',end=' ')
#     else:
#       print(' ',end=' ')
#   print()

# #Print the pattern T.
# n=int(input('Enter a value:'))

# for i in range(1,n+1): #rows
#   for j in range(1,n+1): #columns
#     if i==1 or j==n//2+1:
#       print('*',end=' ')
#     else:
#       print(' ',end=' ')
#   print()


  # print the pattern L

# n=int(input('Enter a value:'))

# for i in range(1,n+1): #rows
#   for j in range(1,n+1): #columns
#     if i==n or j==1:
#       print('*',end=' ')
#     else:
#       print(' ',end=' ')
#   print()

#print the pattern left angle triangle with hollow inside

# n=int(input('Enter a value:'))

# for i in range(1,n+1): #rows
#   for j in range(1,n+1): #columns
#     if i==1 or j==1 or i+j==n+1 :
#       print('*',end=' ')
#     else:
#       print(' ',end=' ')
#   print()

# print a trangle pattern with hollow inside
# n=int(input('Enter a value:'))
# c=2*n-1
# for i in range(1,n+1): #rows
#   for j in range(1,c+1): #columns
#     if i==n or j-i==n-1 or i+j==n+1 :
#       print('*',end=' ')
#     else:
#       print(' ',end=' ')
#   print()


# print a right angle triangle pattern with hollow inside

# n=int(input('Enter a value:'))
# for i in range(1,n+1): #rows
#   for j in range(1,n+1): #columns
#     if i==n or j==n or i+j==n+1 :
#       print('*',end=' ')
#     else:
#       print(' ',end=' ')
#   print()