class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.name=rollno

    def show(self):
        print(self.name,self.rollno)


s1=Student('satya',12)
s2=Student('ankit',14)

print(s1.show())
