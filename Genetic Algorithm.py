#Genetic Algorithm
import random

def fitness(x):
    return x**2

def initialize_population(size):
    return [[random.randint(0,1) for _ in range(5)] for _ in range(size)]

def decode(ch):
    return int("".join(map(str,ch)),2)

def selection(population):
    p1=random.choice(population)
    p2=random.choice(population)
    return max([p1,p2],key=lambda x:fitness(decode(x)))

def crossover(p1,p2):
    point=random.randint(1,4)
    return p1[:point]+p2[point:]

def genetic_algorithm():
    generations=int(input("Enter number of generations: "))
    population=initialize_population(10)
    best=None
    mutation_rate=0.1

    for gen in range(generations):
        new_population=[]

        for i in range(10):
            p1=selection(population)
            p2=selection(population)

            child=crossover(p1,p2)

            for j in range(5):
                if random.random()<mutation_rate:
                    child[j]=1-child[j]

            new_population.append(child)

        population=new_population

        current_best=max(population,key=lambda x:fitness(decode(x)))

        if best is None or fitness(decode(current_best))>fitness(decode(best)):
            best=current_best.copy()

        print("\nGeneration:",gen+1)
        print("Best Chromosome:",current_best)
        print("Best Solution:",decode(current_best))
        print("Best Fitness:",fitness(decode(current_best)))

    print("\n========== FINAL RESULT ==========")
    print("Best Chromosome:",best)
    print("Best Solution:",decode(best))
    print("Best Fitness:",fitness(decode(best)))

genetic_algorithm()
