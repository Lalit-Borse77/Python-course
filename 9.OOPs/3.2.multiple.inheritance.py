# add sub

# class child:
#     def add(self):
#         print("the sum is :-",self.a+self.b)
# class child2:
#     def sub(self):
#         print("the sub is :-",self.a-self.b)
# class father(child,child2):
#     a=int(input("enter the number :-"))
#     b=int(input("enter the number :-"))
# run=father()
# run.add()
# run.sub()

# add mul

# class child:
#     a=10
#     b=5
# class child2:
#     def add(self):
#         print(self.a+self.b)
# class father(child,child2):
#     def mul(self):
#         print(self.a*self.b)
# run=father()
# run.add()
# run.mul()

# mul div

# class child:
#     a=int(input("Enter the number :-"))
#     b=int(input("Enter the number :-"))
# class child2:
#     def mul(self):
#         print(self.a*self.b)
# class father(child,child2):
#     def div(self):
#         print(self.a/self.b)
# run=father()
# run.mul()
# run.div()

# task 1   even odd # positive negative

# class child:
#     a=int(input("Enter the number :-"))
#     b=int(input("Enter the number :-"))
# class child2:
#     def even(self):
#         if self.a%2==0:
#             print("even")
#         else:
#             print("odd")
# class father(child,child2):
#     def positive(self):
#         if self.b>0:
#             print("positive")
#         else:
#             print("negative")
# run=father()
# run.even()
# run.positive()

# task 2 month week

# class child:
#     a=int(input("enter the number :-"))
# class child2:
#     def month(self):
#         if(self.a==1):
#             print("january")
#         elif(self.a==2):
#             print("february")
#         elif(self.a==3):
#             print("March")
#         elif(self.a==4):
#             print("April")
#         elif(self.a==5):
#             print("May")
#         elif(self.a==6):
#             print("June")
#         elif(self.a==7):
#             print("july")
#         elif(self.a==8):
#             print("august")
#         elif(self.a==9):
#             print("september")
#         elif(self.a==10):
#             print("october")
#         elif(self.a==11):
#             print("november")
#         else:
#             print("December")
# class father(child,child2):
#     def week(self):
#         if self.a==1:
#             print("monday")
#         elif self.a==2:
#             print("tuesday")
#         elif self.a==3:
#             print("wednesday")
#         elif self.a==4:
#             print("thursday")
#         elif self.a==5:
#             print("friday")
#         elif self.a==6:
#             print("saturday")
#         elif self.a==7:
#             print("sunday")
#         else:
#             print("write index between 1 to 7")
# run=father()
# run.month()
# run.week()