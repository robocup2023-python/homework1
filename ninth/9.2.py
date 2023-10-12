class Point:
    def __init__(self,x,y,z=0):
        self.x=x;self.y=y;self.z=z
        print("establish Point({}, {}, {})".format(x,y,z))
    def __del__(self):
        print("Del Point({}, {}, {})".format(self.x,self.y,self.z))
    def __add__(self,other):
        if isinstance(other,Vecter):
            return Point(self.x+other.x,self.y+other.y,self.z+other.z)
        elif isinstance(other,Point):
            raise ValueError("Points cannot be added together!")
        else:
            raise TypeError("Unsupported operand type(s)")
    def __sub__(self,other):
        if isinstance(other,Vecter):
            return Point(self.x-other.x,self.y-other.y,self.z-other.z)
        elif isinstance(other,Point):
            return Vecter(self.x-other.x,self.y-other.y,self.z-other.z)
        else:
            raise TypeError("Unsupported operand type(s)")
    def __str__(self):
        return "Point({}, {}, {})".format(self.x,self.y,self.z)
    def __eq__(self,other):
        
        return self.x==other.x and self.y==other.y and self.z==other.z
    def __lt__(self,other):
        import math
        if isinstance(other ,Vecter) or isinstance(other, Point):
            return math.sqrt(self.x**2+self.y**2+self.z**2)<math.sqrt(other.x**2,other.y**2+other.z**2)
        else:
            raise TypeError("Unsupported operand type(s)")
            
        
class Vecter:
    def __init__(self,x,y,z=0):
        self.x=x;self.y=y;self.z=z
        print("establish Vecter({}, {}, {})".format(x,y,z))
    def __del__(self):
        print("Del Vecter({}, {}, {})".format(self.x,self.y,self.z))
    def __add__(self,other):
        if isinstance(other,Point):
            return TypeError("Unsupported operand type(s)")
        elif isinstance(other,Vecter):
            return Vecter(self.x+other.x,self.y+other.y,self.z+other.z)
        else:
            raise TypeError("Unsupported operand type(s)")
    def __sub__(self,other):
        if isinstance(other,Vecter):
            return Vecter(self.x-other.x,self.y-other.y,self.z-other.z)
        else:
            raise TypeError("Unsupported operand type(s)")
    def __eq__(self,other):
        if isinstance(other,Vecter):
            return self.x==other.x and self.y==other.y and self.z==other.z
        else:
            return False
    def __str__(self):
        return "Point({}, {}, {})".format(self.x,self.y,self.z)
        
    
    

        


        

    