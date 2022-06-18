#Two particle system
from matplotlib import animation
import numpy as np
import matplotlib.pyplot as plt

G = 1

dt = 1 
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
        self.velocity = np.array((self.Vx,self.Vy))

    def setCalculated(self,flag):
        self.calculated = flag

class Simulation:
    def __init__(self,particles):
        self.particles = particles

    def calculateDistance(self,Pa,Pb):
        r = np.sqrt((Pa.X-Pb.X)**2 + (Pa.Y-Pb.Y)**2)
        return r

    def calculateForce(self,p1,p2,r):
        gForce = G * p1.mass * p2.mass / r**2
        angle = np.arctan2(p1.Y-p2.Y,p1.X-p2.X)
        fVect = np.array((gForce*np.cos(angle),gForce*np.sin(angle)))
        return fVect

    def updateAcceleration(self,fVect,p):
        p.Ax = fVect[0]/p.mass
        p.Ay = fVect[1]/p.mass
        
    def updateVelocity(self,p):
        p.Vx += p.Ax * dt
        p.Vy += p.Ay * dt

    def updatePosition(self,p):
        p.X +=p.Vx * dt
        p.Y +=p.Vy * dt
    
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

p1 = Particle(100,0,0)
p2 = Particle(20,-50,100,Vx=1,Vy=1)
p3 = Particle(100,50,-25,Vx=-1,Vy=3)
#p4 = Particle(200,-500,100,Vx=20)

particleSet = [p1,p2,p3]
sim = Simulation(particleSet)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)


def animate(i):
    sim.simulate()
    coordinates = sim.positions()
    #if i%20 == 0:
    ax.clear()
    ax.scatter(coordinates[0],coordinates[1],color=('red','green','blue'))
    
    '''
    ax.quiver(coordinates[0][1],coordinates[1][1],p2.Ax,p2.Ay,color='red') #2
    ax.quiver(coordinates[0][1],coordinates[1][1],p2.Vx,p2.Vy,color='green') #2

    ax.quiver(coordinates[0][0],coordinates[1][0],p1.Ax,p1.Ay,color='red') #1
    ax.quiver(coordinates[0][0],coordinates[1][0],p1.Vx,p1.Vy,color='green') #1

    #ax.quiver(p3.X,p3.Y,p3.Ax,p3.Ay,color='red') #3
    #ax.quiver(p3.X,p3.Y,p3.Vx,p3.Vy,color='green') #3'''

    plt.xlim([-500,500])
    plt.ylim([-10,500])
    if i == 500:
        i = 0
ani = animation.FuncAnimation(fig,animate, interval=10)
plt.show()
