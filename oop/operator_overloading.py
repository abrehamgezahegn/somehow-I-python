class Vector: 
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def __add__(self , other):
        return Vector(self.a + other.a , self.b + other.b)
    
    def __mul__(self, other):
        a = self.a * other.a
        b = self.b * other.b
        return Vector(a,b)
   
    def get_vector(self):
        print(f"({self.a},{self.b})")  
    
v1 = Vector(1,4)
v2 = Vector(3,5)

# addition operator
v3 = v1 + v2
v3.get_vector()

#multiply operator
v4 = v1 * v2
v4.get_vector()



# Addition	    p1 + p2	    p1.__add__(p2)
# Subtraction	p1 - p2	    p1.__sub__(p2)
# Multiplication	p1 * p2	p1.__mul__(p2)
# Power	p1 ** p2	p1.__pow__(p2)
# Division	p1 / p2	p1.__truediv__(p2)
# Floor Division	p1 // p2	p1.__floordiv__(p2)
# Remainder (modulo)	p1 % p2	p1.__mod__(p2)
# Bitwise Left Shift	p1 << p2	p1.__lshift__(p2)
# Bitwise Right Shift	p1 >> p2	p1.__rshift__(p2)
# Bitwise AND	p1 & p2	p1.__and__(p2)
# Bitwise OR	p1 | p2	p1.__or__(p2)
# Bitwise XOR	p1 ^ p2	p1.__xor__(p2)
# Bitwise NOT	~p1	p1.__invert__()


