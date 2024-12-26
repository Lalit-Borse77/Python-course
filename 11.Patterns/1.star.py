# left half star

# i=1
# while i<=10:
#     j=1
#     while j<=i:
#         print(j,end="")
#         j=j+1
#     print()
#     i=i+1

# for i in range(1,6,1):
#         for j in range(5-i):
#                 print(" ",end=" ") 
#         for k in range(i*2-1):
#                 print("* ",end="")
#         print(""*i)

# for i in range(1,6,1):
#         for j in range(6-i):
#                 print(i,end="")
#         print(i,end="")

# i=1
# n=1
# while i<=4:
#         j=1
#         while j<=5-i:
#                 print("  ",end="")
#                 j=j+1
#         k=1
#         while k<=i:
#                 print(n+i,end=" ")
#                 n += 1
#                 k += 1
#         print()
#         i +=i

# n = 1
# i = 1
# while i <= 4:
#     str = ""
#     j = 1
#     while j <= 4 - i:
#         str += " "
#         j += 1
#     k = 1
#     while k <= i:
#         str += str(n) + " "
#         n += 1
#         k += 1
#     print(str)
#     i += 1

# user define

# i=1
# n=int(input("enter :"))
# while i<=n:
#     j=1
#     while j<=i:
#         print("* ",end="")
#         j=j+1
#     print()
#     i=i+1

# i=4
# while i>=1:
#     j=1
#     while j<=i:
#         k=1
#         while k<=2 * i - 1:
#             print("* ",end="")
#             k=k+1
#             print()
#         j=j+1
#     print()
#     i=i-1







i=5
while i>=1:
    j=i
    while j<=5-1:
        j=j+1
        print(" ",end=" ")
    k=1
    while k<=2*i-1:
        k=k+1
        print("* ",end="")
    i=i-1
    print()