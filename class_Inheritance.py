class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = list()
    def input_sides(self):
        self.sides = [float(input('Enter side' + str(i+1) + ':')) for i in range(self.n)]
    def disp_sides(self):
        for i in range(self.n):
            print('side', i + 1, 'is', self.sides[i])
class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)
    def find(self):
        a, b, c = self.sides
        try:
            if a+b > c and a+c > b and b+c > a:
        except Exception:
            print('Error_1')

class Triangle_rect(Triangle):
    def __init__(self):
        super().__init__()
    def find_area(self):
        a, b, c = self.sides
        if a**2+b**2+c**2 == 2*max(a, b, c)**2:
            self.sides.remove(max(self.sides))
            area = 0.5 * self.sides[0] * self.sides[1]
        else:
            s = (a + b + c) / 2
            area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)

tr_area = Triangle_rect()
tr_area.input_sides()
tr_area.disp_sides()
tr_area.find()
tr_area.find_area()



