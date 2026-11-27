#Gene Expression
import random

# User input
n = int(input("Enter number of appliances: "))

appliances = []
power = []
comfort = []

for i in range(n):
    name = input("\nEnter appliance name: ")
    p = float(input("Enter power consumption (Watts): "))
    c = int(input("Enter comfort value (1-10): "))

    appliances.append(name)
    power.append(p)
    comfort.append(c)

min_comfort = int(input("\nEnter minimum comfort required: "))

population_size = 10
generations = int(input("Enter number of generations: "))
mutation_rate = 0.1

# Generate initial population
def initialize_population():
    return [[random.randint(0, 1) for _ in range(n)]
            for _ in range(population_size)]

# Calculate fitness
def fitness(chromosome):
    total_power = sum(chromosome[i] * power[i] for i in range(n))
    total_comfort = sum(chromosome[i] * comfort[i] for i in range(n))

    if total_comfort < min_comfort:
        return float('inf')

    return total_power

# Selection
def selection(population):
    p1, p2 = random.sample(population, 2)
    return min([p1, p2], key=fitness)

# Crossover
def crossover(p1, p2):
    point = random.randint(1, n - 1)
    return p1[:point] + p2[point:]

# Mutation
def mutation(child):
    for i in range(n):
        if random.random() < mutation_rate:
            child[i] = 1 - child[i]
    return child

# Genetic Algorithm
def genetic_algorithm():
    population = initialize_population()
    best = None

    for gen in range(generations):
        new_population = []

        for i in range(population_size):
            p1 = selection(population)
            p2 = selection(population)

            if n > 1:
                child = crossover(p1, p2)
            else:
                child = p1.copy()

            child = mutation(child)
            new_population.append(child)

        population = new_population

        current_best = min(population, key=fitness)

        if best is None or fitness(current_best) < fitness(best):
            best = current_best.copy()

    # Display result
    print("\n===== OPTIMAL ELECTRICITY SETTINGS =====")

    total_power = 0
    total_comfort = 0

    for i in range(n):
        status = "ON" if best[i] == 1 else "OFF"
        print(appliances[i], ":", status)

        total_power += best[i] * power[i]
        total_comfort += best[i] * comfort[i]

    print("\nTotal Power Consumption:", total_power, "Watts")
    print("Total Comfort Level:", total_comfort)
    print("Minimum Required Comfort:", min_comfort)

    if total_comfort >= min_comfort:
        print("Status: Comfort Requirement Satisfied")
    else:
        print("Status: No Feasible Solution Found")

    print("========================================")


genetic_algorithm()
