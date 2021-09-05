import math

class Line:

    def __init__(self, coord1, coord2):
        self.coord_x, self.coord_y = coord1
        self.coord2_x, self.coord2_y = coord2
    
    def distance(self):
        point_dis = math.sqrt((self.coord2_x - self.coord_x)**2 + (self.coord2_y - self.coord_y)**2)
        return point_dis
        
    def slope(self):
        point_slope = (self.coord2_y - self.coord_y) / (self.coord2_x - self.coord_x)
        return point_slope


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

print(li.distance())
print(li.slope())