class Student:
    clg="KLU"
    """docstring for Classname"""
    def __init__(self,arg):
        super().__init__(self,id,name,course)
        self.id=id
        self.name=name
        self.course=course
    def display(self,):
        print(f"self.this is{self.id}")
        print(f"self.this is{self.name}")
        print(f"self.this is{self.course}")

s1 = Student(12345,"Keerthana","PFSD")
print(s1)