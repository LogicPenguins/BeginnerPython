import math

class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        cylinder_vol = self.height * math.pi * self.radius**2
        return round(cylinder_vol, 2)

    def surface_area(self):
        sa = (2 * math.pi * self.radius**2) + self.height * (2 * math.pi * self.radius)
        return round(sa, 2)

c = Cylinder(2, 3)

print(c.volume())
print(c.surface_area())