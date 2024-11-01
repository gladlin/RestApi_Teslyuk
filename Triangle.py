class TriangleChecker:
    def __init__(self, a = 0, b = 0, c = 0):
        self.a = a
        self.b = b
        self.c = c
    
    def is_triangle(self):
        try:
            val = int(self.a)
            val = int(self.b)
            val = int(self.c)
        except:     
            print("Enter only integer please!")
            return
        
        if(self.a <= 0 or self.b <= 0 or self.c <= 0):
            print("Please, enter positive integers")
            return
        
        if((self.a > self.b + self.c) or
           (self.b > self.a + self.c) or
           (self.c > self.b + self.a)):
            print("Жаль, треугольник из этого не сделать")
        else:
            print("Ура, можно построить треугольник!")
        



treugol = TriangleChecker(2, 4, 5)
treugol.is_triangle()