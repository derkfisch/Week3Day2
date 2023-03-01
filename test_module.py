print("this is the test module")

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self, radius):
        return 3.14*(self.radius ** 2)
    
class Hypotenuse:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def finding_c(self):
        return (self.a ** 2) + (self.b ** 2)
    
# I got the import to work for test_module in Jupiter Notebook
# Did not get the functions to work for returning area / hypotenuse
    
