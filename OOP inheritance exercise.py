class shape :
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2


class triangle(shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("AREA of triangle = ",area)


class rectangle(shape):
    def area(self):
        area =  self.dim1 * self.dim2
        print("AREA of rectangle = ",area)


t = triangle(20,30)
t.area()

r = rectangle(20,30)
r.area()