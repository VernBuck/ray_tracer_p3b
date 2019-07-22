class surface_material(object):
    # each 3d object has position as surface
    def __init__(self,Crd,Cdg,Cdb,Car,Cag,Cab,Csr, Csg, Csb, P, Krefl):
        self.Crd = Crd
        self.Cdg = Cdg
        self.Cdb = Cdb
        self.Car = Car
        self.Cag = Cag
        self.Cab = Cab
        self.Csr = Csr
        self.Csg = Csg
        self.Csb = Csb
        self.P = P
        self.Krefl = Krefl
        