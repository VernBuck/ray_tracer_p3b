#make another object for diffuse colors
class intersection_point(object):
    def __init__(self,ray, object, minVal, bool, dx, dy, dz):
        #iterate through each 3d model in list
        type = object.textShape
        if(type == 'sphere'):
            #sphere logic
            x1 = object.x
            y1 = object.y
            z1 = object.z
            r1 = object.r
    
            x = ray.direction.x
            y = ray.direction.y
            z = ray.direction.z
    
            a = ((x)*(x)) + ((y)*(y)) + ((z)*(z))
            b = -2 * (((x)*(x1)) + ((y)*(y1)) + ((z)*(z1)))
            c = ((x1)*(x1)) + ((y1)*(y1)) +((z1)*(z1)) - ((r1)*(r1)) 
   
            if ((b*b) - ((4)*(a)*(c)) < 0):
            # print("here")
                bool = False
                self.bool = bool
                return
            t = (-1*b + ((b*b) - ((4)*(a)*(c)))**(0.5))/ (2 * a)
            t2 = (-1*b - ((b*b) - ((4)*(a)*(c)))**(0.5))/ (2 * a)
        
        
        # print("pie")
            tTrue = min(abs(t),abs(t2))
            minVal = tTrue
            self.minVal = minVal
            self.object = object
            self.bool = bool
            self.dx = x
            self.dy = y
            self.dz = z
        if(type == 'triangle'):
            #referenced Ray-triangle intersection Brian Curless 
            x1 = object.x #vertex 1 A
            y1 = object.y #vertex 2 B
            z1 = object.z #vertex 3 C
            
            
            # q is the point of intersection
            x = ray.direction.x
            y = ray.direction.y
            z = ray.direction.z
            # ray direction arrow
            edgeA = y1 - x1
            edgeB = z1 - x1
            
            # n
            #edgeAB = edgeA*edgeB
            edgeAB = PVector.cross(edgeA,edgeB)
            #if (edgeAB == 0): check magnitude
                #bool = False
                #self.bool = bool
                #return
            n = (edgeAB) / ((edgeAB).mag())
            d = PVector.dot(x1, n)
            
           # p = PVector(x,y,z)
            
            #check = (PVector.dot(n,ray.direction))
            #println(check)
            #println(x)
            #println(
            
            if (PVector.dot(n,ray.direction) == 0):
                bool = False
                self.bool = bool
                return
            denominator = (PVector.dot(n,ray.direction))
            if (denominator <= 0):
                bool = False
                self.bool = bool
                return
            numerator = (PVector.dot(n, x1 - ray.starting_point))
            t = numerator/denominator
            #t = (d - (PVector.dot(n,ray.starting_point)))/(PVector.dot(n,ray.direction))
            # Q point of potential intersection
            if (t <= 0):
                bool = False
                self.bool = bool
                return
            q = ray.starting_point + (PVector.mult(ray.direction, t)) #t * d
            
            #test for inside
            edgeQ1 = q - x1
            testQ1 = PVector.dot((PVector.cross(edgeA, edgeQ1)), n)
            if (testQ1 < 0):
                bool = False
                self.bool = bool
                return
            edgeQ2 = q - y1
            edgeC = (z1 - y1)
            edgeD = (x1 - z1)
            testQ2 = PVector.dot((PVector.cross(edgeC, edgeQ2)), n)
            if (testQ2 < 0):
                bool = False
                self.bool = bool
                return
            edgeQ3 = q - z1
            testQ3 = PVector.dot((PVector.cross(edgeD, edgeQ3)), n)
            if (testQ3 < 0):
                bool = False
                self.bool = bool
                return
            
            minVal = t
            self.minVal = minVal
            self.object = object
            self.bool = bool
            self.dx = x
            self.dy = y
            self.dz = z