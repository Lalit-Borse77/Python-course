#hierarchical inheritance

# class father:
#     def add(self):
#         print("the sum is :-",self.a+self.b+self.c+self.d+self.e)
# class son:
#     a=10
# class son2:
#     b=20
# class son3:
#     c=30
# class son4:
#     d=40
# class son5(father,son,son2,son3,son4):
#     e=50
# run=son5()
# run.add()

class father:
    def add(self):
        print("the sum is :-",self.a+self.b+self.c+self.d+self.e)
class son:
    a=10
class son2:
    b=20
class son3:
    c=30
class son4:
    d=40
class son5(father,son,son2,son3,son4):
    e=50
run=son5()
run.add()