import random

def fitness(individual, weights, values, max_weight):
    value = 0
    weight = 0
    for i in range(len(individual)):
        if individual[i] == 1:
            weight += weights[i]
            value += values[i]
    if weight > max_weight:
        return 0
    else:
        return value

def generate_population(pop_size, item_count):
    population = []
    for i in range(pop_size):
        population.append([random.randint(0, 1) for i in range(item_count)])
    return population

def tournament_selection(population, weights, values, max_weight):
    tournament_size = 2
    chosen = []
    for i in range(tournament_size):
        random_index = random.randint(0, len(population) - 1)
        chosen.append(population[random_index])
    return max(chosen, key=lambda x: fitness(x, weights, values, max_weight))

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutation(individual):
    mutation_chance = 0.01
    for i in range(len(individual)):
        if random.random() < mutation_chance:
            individual[i] = 1 - individual[i]
    return individual

def genetic_algorithm(weights, values, max_weight, pop_size=100, generations=100):
    population = generate_population(pop_size, len(weights))
    for generation in range(generations):
        new_population = []
        for i in range(pop_size):
            parent1 = tournament_selection(population, weights, values, max_weight)
            parent2 = tournament_selection(population, weights, values, max_weight)
            child = crossover(parent1, parent2)
            child = mutation(child)
            new_population.append(child)
        population = new_population
    best_fit = max(population, key=lambda x: fitness(x, weights, values, max_weight))
    return best_fit

weights = [10, 20, 30]
values = [60, 100, 120]
max_weight = 50

best = genetic_algorithm(weights, values, max_weight)
value = fitness(best, weights, values, max_weight)
print(f"Best solution: {best}")
print(f"Value: {value}")
