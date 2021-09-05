class Student :
    name = " "
    roll = " "
    cgpa = " "

    def __init__(self,name,roll,cgpa):
        self.name = name
        self.roll = roll
        self.cgpa = cgpa

    def display(self):
        print(f"Name : {self.name}, Roll : {self.roll}, CGPA : {self.cgpa}")

d = Student("mahadi",177,3.46)
d.display()

s = Student("sadia",444,3.88)
s.display()