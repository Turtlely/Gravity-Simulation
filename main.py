import plot, Particle

#Initiate particles

p1 = Particle.Particle(10,0,0)
p2 = Particle.Particle(10,-250,0,Vy=-1)
p3 = Particle.Particle(10,250,0,Vy=1)
p4 = Particle.Particle(10,0,250,Vx=-1)
p5 = Particle.Particle(10,0,-250,Vx=1)

particles = [p1,p2,p3,p4,p5]

#Start simulation
anim = plot.plotter(particles)

anim.init_sim()
