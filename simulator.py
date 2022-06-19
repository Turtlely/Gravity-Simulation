#Two particle system
import numpy as np
import const

class Simulation:
    def __init__(self,particles):
        self.particles = particles

    def getParticles(self):
        return self.particles

    def calculateDistance(self,Pa,Pb):
        r = np.sqrt((Pa.X-Pb.X)**2 + (Pa.Y-Pb.Y)**2)
        return r

    def calculateForce(self,p1,p2,r):
        gForce = const.G * p1.mass * p2.mass / r**2
        angle = np.arctan2(p1.Y-p2.Y,p1.X-p2.X)
        fVect = np.array((gForce*np.cos(angle),gForce*np.sin(angle)))
        return fVect

    def updateAcceleration(self,fVect,p):
        p.Ax = fVect[0]/p.mass
        p.Ay = fVect[1]/p.mass
        
    def updateVelocity(self,p):
        p.Vx += p.Ax * const.dt
        p.Vy += p.Ay * const.dt

    def updatePosition(self,p):
        p.X +=p.Vx * const.dt
        p.Y +=p.Vy * const.dt
    
    def simulate(self):
        '''
        loop through set of particles
        calculate forces between every pair of particles
        update accelerations, velocities, and positions
        '''
        for p1 in self.particles:
            if p1.calculated == True:
                continue
                        
            p1.setCalculated(True)
            for p2 in self.particles:
                #calculate force between p1 and p2
                #prevent double counting of pairs, p1p2 is same as p2p1

                if p2.calculated == True:
                    continue

                else:
                    r = self.calculateDistance(p1,p2)
                    fVect12 = self.calculateForce(p1,p2,r)
                    fVect21 = self.calculateForce(p2,p1,r)
                    
                    #update p1
                    self.updateAcceleration(fVect21,p1)

                    #update p2
                    self.updateAcceleration(fVect12,p2)

                    self.updateVelocity(p1)
                    self.updateVelocity(p2)

                    self.updatePosition(p1)
                    self.updatePosition(p2)

                    p2.calculated = True
        
        for p in self.particles:
            p.setCalculated(False)

    def positions(self):
        x = []
        y = []
        for p in self.particles:
            x.append(p.X)
            y.append(p.Y)
        return x,y
