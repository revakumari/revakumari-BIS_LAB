#Grey Wolf Optimiser
import random

# User input
current_moisture = float(input("Enter current soil moisture (%): "))
desired_moisture = float(input("Enter desired soil moisture (%): "))
max_water = float(input("Enter maximum irrigation water (litres): "))

# GWO parameters
wolves = 10
iterations = int(input("Enter number of iterations: "))

# Fitness function
def fitness(water):
    final_moisture = current_moisture + (water * 0.5)

    if final_moisture < desired_moisture:
        penalty = (desired_moisture - final_moisture) * 100
        return water + penalty

    return water


# Initialize wolf positions
positions = [random.uniform(0, max_water)
             for _ in range(wolves)]

# Grey Wolf Optimizer
def GWO():

    global positions

    for iteration in range(iterations):

        # Find Alpha, Beta and Delta wolves
        sorted_wolves = sorted(positions, key=fitness)

        alpha = sorted_wolves[0]
        beta = sorted_wolves[1]
        delta = sorted_wolves[2]

        # Control parameter
        a = 2 - (2 * iteration / iterations)

        new_positions = []

        for wolf in positions:

            r1 = random.random()
            r2 = random.random()

            A1 = 2 * a * r1 - a
            C1 = 2 * r2

            D_alpha = abs(C1 * alpha - wolf)
            X1 = alpha - A1 * D_alpha

            r1 = random.random()
            r2 = random.random()

            A2 = 2 * a * r1 - a
            C2 = 2 * r2

            D_beta = abs(C2 * beta - wolf)
            X2 = beta - A2 * D_beta

            r1 = random.random()
            r2 = random.random()

            A3 = 2 * a * r1 - a
            C3 = 2 * r2

            D_delta = abs(C3 * delta - wolf)
            X3 = delta - A3 * D_delta

            # Update wolf position
            new_wolf = (X1 + X2 + X3) / 3

            # Keep water within limits
            new_wolf = max(0, min(max_water, new_wolf))

            new_positions.append(new_wolf)

        positions = new_positions

    # Find best solution
    best_water = min(positions, key=fitness)
    final_moisture = current_moisture + (best_water * 0.5)

    print("\n===== SMART IRRIGATION OPTIMIZATION =====")
    print("Current Soil Moisture:", current_moisture, "%")
    print("Desired Soil Moisture:", desired_moisture, "%")
    print("Optimal Water Required:", round(best_water, 2), "litres")
    print("Final Soil Moisture:", round(final_moisture, 2), "%")

    if final_moisture >= desired_moisture:
        print("Status: Moisture Requirement Satisfied")
    else:
        print("Status: Insufficient Water Capacity")

    print("=========================================")


GWO()
