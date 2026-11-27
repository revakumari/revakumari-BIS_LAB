#Cuckoo Search

import random
import math

n = int(input("Enter number of customer locations: "))

locations = ["Warehouse"]

for i in range(1, n + 1):
    locations.append("Customer " + str(i))

print("\nEnter distance matrix:")

distances = []

for i in range(n + 1):
    row = list(map(int, input().split()))
    distances.append(row)

nests = int(input("\nEnter number of nests: "))
iterations = int(input("Enter number of iterations: "))

pa = 0.25
beta = 1.5

def fitness(route):
    total = 0

    for i in range(len(route) - 1):
        total += distances[route[i]][route[i + 1]]

    total += distances[route[-1]][route[0]]

    return total


def generate_route():
    route = list(range(1, n + 1))
    random.shuffle(route)
    return [0] + route


def levy_flight(route):
    new_route = route.copy()

    if n < 2:
        return new_route

    sigma = (
        math.gamma(1 + beta) * math.sin(math.pi * beta / 2) /
        (math.gamma((1 + beta) / 2) * beta *
         2 ** ((beta - 1) / 2))
    ) ** (1 / beta)

    u = random.gauss(0, sigma)
    v = random.gauss(0, 1)

    step = u / (abs(v) ** (1 / beta) + 1e-10)

    swaps = max(1, min(n, int(abs(step) * n) + 1))

    for _ in range(swaps):
        i, j = random.sample(range(1, n + 1), 2)
        new_route[i], new_route[j] = new_route[j], new_route[i]

    return new_route


def cuckoo_search():

    population = [generate_route() for _ in range(nests)]

    best_route = min(population, key=fitness)
    best_distance = fitness(best_route)

    for iteration in range(iterations):

        for i in range(nests):

            new_route = levy_flight(population[i])

            j = random.randrange(nests)

            if fitness(new_route) < fitness(population[j]):
                population[j] = new_route

        population.sort(key=fitness)

        abandon = max(1, int(pa * nests))

        for i in range(nests - abandon, nests):
            population[i] = generate_route()

        current_best = min(population, key=fitness)

        if fitness(current_best) < best_distance:
            best_route = current_best.copy()
            best_distance = fitness(best_route)

    route_names = [locations[i] for i in best_route]
    route_names.append("Warehouse")

    print("\n===== DELIVERY ROUTE OPTIMIZATION =====")

    print("Best Route:", " -> ".join(route_names))
    print("Minimum Distance:", best_distance, "km")
    print("Number of Nests:", nests)
    print("Iterations:", iterations)

    print("=======================================")


cuckoo_search()
