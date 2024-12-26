#  1 to 10
# for i in range(1,11,1):
#     print("*"*i)

# name print
# for i in range(1,5,1):
#     print("aman")

# #simple table
# for i in range(2,21,2):
#     print(i)    


# # 1 to n
# n=int(input("enter the number:"))
# for i in range(1,n,1):
#     print(i)

# # 10 to 1
# for i in range(11,0,-1):
#     print(i)

# #user define table
# n=int(input("enter the any table:-"))
# for i in range(1,11,1):
#     {
#         print(i*n)
#     }

# #even
# for i in range(2,20,2):
#     if(i%2==0):
#         {
#             print(i)
#         }

# #odd
# for i in range(1,21,2):
#     if(i%2!=0):
#         print(i)

# #user define even
# r=int(input("Enter the number :-"))
# for i in range(1,r,1):
#     if(i%2==0):
#         print(i)

# #user define odd
# q=int(input("Enter the number :"))
# for i in range(1,q,1):
#     if(i%2!=0):
#         print(i)

#patterns

# for i in range(1,11,1):
#     print("*"*i)

# rows = 5
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print("\r")

# rows = 5
# k = 2 * rows - 2
# for i in range(0, rows):
#     # process each column
#     for j in range(0, k):
#         # print space in pyramid
#         print(end=" ")
#     k = k - 2
#     for j in range(0, i + 1):
#         # display star
#         print("* ", end="")
#     print("")
