class Point:
    def __init__(self, X, Y):
        self.x = X
        self.y = Y

    def move(self):
        print("move", self.x, self.y)
    
    def draw(self):
        print("draw")    

point1 = Point(4,5)
point1.x = 10
point1.move()

point2 = Point(6, 7)
point2.move()

print(point1.__dict__)
