class Particle:
    def __init__(self,mass,X,Y,Vx=0,Vy=0,Ax=0,Ay=0):
        self.mass = mass
        self.X = X
        self.Y = Y
        self.Vx = Vx
        self.Vy = Vy
        self.Ax = Ax
        self.Ay = Ay
        self.calculated = False
        self.velocity = [self.Vx,self.Vy]

    def setCalculated(self,flag):
        self.calculated = flag
