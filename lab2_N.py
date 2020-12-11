#Импортим генетический алгоритм
from pyeasyga.pyeasyga import GeneticAlgorithm 
import random
import numpy as np

#Представление данных
#Данные представляют из себя множество нулей с одной единицей на какой-либо позиции
#Это позиция отражает положение x на оси абсцисс от -4 до 0
seed_data = [0] * 399
seed_data.append(1)

#Иницилизируем генетический алгоритм с заданными данными, а также размером
#популяции, количеством поколений, шансом на кроссинговер и мутацию
ga = GeneticAlgorithm(seed_data, 400, 200, 0.7, 0.05, True, True)

#Представляем отдельную особь как случайное положение х
def create_individual(data):
    individual = data[:]
    random.shuffle(individual)
    return individual
    
ga.create_individual = create_individual

#Одноточечный кроссинговер
def crossover(parent_1, parent_2):
    crossover_index = random.randrange(1, len(parent_1))
    child_1a = parent_1[:crossover_index]
    child_1b = [i for i in parent_2 if i not in child_1a]
    child_1 = child_1a + child_1b

    child_2a = parent_2[crossover_index:]
    child_2b = [i for i in parent_1 if i not in child_2a]
    child_2 = child_2a + child_2b
    return child_1, child_2

ga.crossover_function = crossover

#Целочисленная мутация
def mutate(individual):
    mutate_index1 = random.randrange(len(individual))
    mutate_index2 = random.randrange(len(individual))
    individual[mutate_index1], individual[mutate_index2] = individual[mutate_index2], individual[mutate_index1]

ga.mutate_function = mutate

#Рулеточная селекция
def selection(population):
    return random.choice(population)


ga.selection_function = selection

#Реализация функции приспособленности
#Ищет такой х, при котором значение функции максимально
def fitness (individual, data):
    fitness = -float("inf")
    x = -4
    for item in individual:
        if item != 1:
            x += 0.01
        else:
            fitness = 1 / x
            break 
    return fitness

ga.fitness_function = fitness
ga.run()
print(ga.best_individual()) #Выводит самую приспособленную особь