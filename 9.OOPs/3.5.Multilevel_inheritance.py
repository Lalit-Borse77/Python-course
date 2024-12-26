# multilevel inheritance

# class child:
#     a=10
# class child2(child):
#     b=20
# class father(child2):
#     def add(self):
#         print(self.a+self.b)
# run=father()
# run.add()

# class child:
#     a=10
# class child2(child):
#     a=20
# class father(child2):
#     def sub(self):
#         if(self.a>0):
#             print("pos")
#         else:
#             print("neg")
# run=father()
# run.sub()

class child:
    a=10
class child2(child):
    b=20
class father(child2):
    def sub(self):
            print(self.a+self.b)
run=father()
run.sub()