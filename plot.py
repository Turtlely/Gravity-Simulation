import matplotlib.pyplot as plt
from matplotlib import animation
import Particle as Particle
import simulator as Simulation
import const

class plotter():
    def __init__(self,particles):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1,1,1)
        self.particles = particles
        self.sim = Simulation.Simulation(particles)

    def init_sim(self):
        a=animation.FuncAnimation(self.fig,self.animate, interval=10)
        plt.show()

    def animate(self,i):
        self.sim.simulate()
        
        #get coordinates of all point
        coordinates = self.sim.positions()

        self.ax.clear()
        self.ax.scatter(coordinates[0],coordinates[1])
        
        for p in self.sim.getParticles():
            self.ax.quiver(p.X,p.Y,p.Ax,p.Ay,color='red')
            self.ax.quiver(p.X,p.Y,p.Vx,p.Vy,color='green')
        '''
        ax.quiver(coordinates[0][1],coordinates[1][1],p2.Ax,p2.Ay,color='red') #2
        ax.quiver(coordinates[0][1],coordinates[1][1],p2.Vx,p2.Vy,color='green') #2

        ax.quiver(coordinates[0][0],coordinates[1][0],p1.Ax,p1.Ay,color='red') #1
        ax.quiver(coordinates[0][0],coordinates[1][0],p1.Vx,p1.Vy,color='green') #1

        #ax.quiver(p3.X,p3.Y,p3.Ax,p3.Ay,color='red') #3
        #ax.quiver(p3.X,p3.Y,p3.Vx,p3.Vy,color='green') #3'''

        plt.xlim(const.xlim)
        plt.ylim(const.ylim)


