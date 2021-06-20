def print_mro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))


class Man:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

class SalesMan:
    def __init__(self, seniority):
        self.seniority = seniority
    
    def get_exp(self):
        return self.seniority

## inheritance by composition
class Dwight(Man, SalesMan):
    def __init__(self, name, seniority, mode):
        Man.__init__(self, name)
        SalesMan.__init__(self, seniority)
        self.mode = mode

    def get_mode(self):
        return self.mode




print_mro(Dwight)

dwight_1 = Dwight("Dwight" , 20,   "farmer")
# print(dwight_1.get_name())
# print(dwight_1.get_exp())
# print("mode" , dwight_1.get_mode())

