class later_triangle(object):
    #add surface material
    def __init__(self,x1,y1,z1,textShape, surfacematerial):
        self.x = x1
        self.y = y1
        self.z = z1
        self.surfacematerial = surfacematerial
        self.textShape = textShape
        
        #
    def normalS(self, interSection):
        
        self.interSection = interSection
        x1 = self.x
        y1 = self.y
        z1 = self.z
        edgeA = y1 - x1
        edgeB = z1 - x1
        edgeAB = PVector.cross(edgeA,edgeB)
        return (edgeAB) / ((edgeAB).mag())