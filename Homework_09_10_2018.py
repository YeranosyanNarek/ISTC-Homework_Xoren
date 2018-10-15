
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = list()
    def input_sides(self):
        self.sides = [float(input('Enter side' + str(i+1) + ':')) for i in range(self.n)]
    def disp_sides(self):
        for i in range(self.n):
            print('side', i + 1, 'is', self.sides[i])
def filter(a, b, c):
    if a ** 2 + b **  2 + c ** 2 == 2 * (max(a, b, c)**2):
        return True
    else:
        return False

class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)

    def find_area(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        if filter(a, b, c):
            self.sides.remove(max(self.sides))
            return 'This is a rectangular triangle:S = %0.2f' % ((self.sides[0] * self.sides[1]) / 2)
        else:
            return 'This is not a rectangular triangle:S = %0.2f' % (s*(s-a)*(s-b)*(s-c)) ** 0.5

tr_area = Triangle()
tr_area.input_sides()
tr_area.disp_sides()
print(tr_area.find_area())

