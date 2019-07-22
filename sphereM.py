class sphereM(object):
    #add surface material
    def __init__(self,x,y,z,textShape, radius, surfacematerial):
        self.x = x
        self.y = y
        self.z = z
        self.r = radius
        self.surfacematerial = surfacematerial
        self.textShape = textShape
        
    def normalS(self, interSection):
        self.interSection = interSection
        center = PVector(self.x,self.y,self.z)
        normalP = interSection - center
        return normalP.normalize()