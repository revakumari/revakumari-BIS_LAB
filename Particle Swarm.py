#Particle Swarm

import random

def fitness(x):
    return x**2

def initialize(n):
    particles=[]
    for i in range(n):
        pos=random.uniform(-10,10)
        vel=random.uniform(-1,1)
        particles.append([pos,vel])
    return particles

def findbest(pbest):
    return max(pbest,key=lambda x:fitness(x))

def pso():
    n=int(input("Enter number of particles: "))
    mx=int(input("Enter number of iterations: "))

    w=0.5
    c1=1.5
    c2=1.5

    particles=initialize(n)

    pbest=[p[0] for p in particles]
    gbest=findbest(pbest)

    for i in range(mx):
        print("\n========== ITERATION",i+1,"==========")

        for j in range(n):
            pos,vel=particles[j]

            fit=fitness(pos)

            if fit>fitness(pbest[j]):
                pbest[j]=pos

            if fit>fitness(gbest):
                gbest=pos

            r1=random.random()
            r2=random.random()

            vel=w*vel+c1*r1*(pbest[j]-pos)+c2*r2*(gbest-pos)

            pos=pos+vel

            particles[j]=[pos,vel]

            print("\nParticle:",j+1)
            print("Position:",round(pos,4))
            print("Velocity:",round(vel,4))
            print("Fitness:",round(fitness(pos),4))
            print("PBest:",round(pbest[j],4))
            print("GBest:",round(gbest,4))

        print("\nBest in Iteration:",round(gbest,4))
        print("Best Fitness:",round(fitness(gbest),4))

    print("\n========== FINAL RESULT ==========")
    print("Global Best Position:",gbest)
    print("Maximum Fitness:",fitness(gbest))

pso()
