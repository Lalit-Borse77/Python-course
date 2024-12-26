# simple example

# class child:
#     a=10
#     b=5
# class child2(child):
#     def add(self):
#         print(self.a+self.b)
# class child3(child):
#     def sub(self):
#         print(self.a-self.b)
# class father(child2,child3):
#     def mul(self):
#         print(self.a*self.b)
# run=father()
# run.add()
# run.sub()
# run.mul()

# even pass positive

# class child:
#     a=1
#     b=39
#     c=-12

# class child2(child):
#     def even(self):
#         if self.a%2==0:
#             print("even")
#         else:
#             print("odd")

# class child3(child):
#     def pas(self):
#         if self.b >= 33:
#             print("pass")
#         else:
#             print("fail")

# class father(child2,child3):
#     def pos(self):
#         if self.c>0:
#             print("positive")
#         else:
#             print("negative")

# run=father()
# run.even()
# run.pas()
# run.pos()

class child():
    a=11
    b=30
    c=1
class child2(child):
    def even(self):
        if self.a%2==0:
            print("even")
        else:
            print("odd")
class child3(child):
    def pas(self):
        if self.b>33:
            print("pass")
        else:
            print("fail")
class father(child3,child2):
    def pos(self):
        if self.c>=0:
            print("positive")
        else:
            print("negative")
run=father()
run.even()
run.pas()
run.pos()