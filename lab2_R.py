from pyeasyga.pyeasyga import GeneticAlgorithm
import random
import numpy as np

data = (-0.5, [-2.0]) #Формат задания значений (y(x), [x])
#Задаём параметры работы генетического алгоритма
ga = GeneticAlgorithm(data, 20, 30, 0.7, 0.01, True, True)
#(начальные данные, количество особей в популяции, количество генераций, вероятность применения оператора скрещивания, вероятность применения мутации к гену, вкл. выбор лучшей особи, максимизация целевой функции)
def create_individual(data): #Функция создания начальной популяции
    ind = [random.uniform(-4.0, -1e-10)] #Вещественное кодирование
    print(1 / ind[0], ind) #Вывод начальной популяции на экран
    return ind #[random.uniform(-4.0, -0.1) for _ in range(len(data))]
    
ga.create_individual = create_individual

def crossover(parent_1, parent_2): #Функция кроссинговера ГА (арифметический кроссинговер, lambda = 0.2)
    child_1 = [parent_1[0] * 0.2 + parent_2[0] * 0.8]
    child_2 = [parent_2[0] * 0.2 + parent_1[0]* 0.8]
    return child_1, child_2

ga.crossover_function = crossover

def mutate(individual): #Функция мутации для вещественного кодирования
    rnd = np.random.normal(0, 0.5)
    if rnd < -0.5:
        rnd = -0.5
    elif rnd > 0.5:
        rnd = 0.5
    individual[0] = individual[0] + rnd

ga.mutate_function = mutate

def selection(population): #Функция селекции (турнирный отбор)
    ind1 = random.choice(population)
    ind2 = random.choice(population)
    if ind1.fitness > ind2.fitness:
        return ind1
    else:
        return ind2

ga.selection_function = selection

def fitness (individual, data): #Целевая функция
    if individual[0] < -4.0: #Ограничения переменных ЦФ
        individual[0] = -4.0
    if individual[0] >= 0:
        individual[0] = 1e-10
    return 1 / individual[0] #Значение целевой функции 
    
ga.fitness_function = fitness
ga.run() #Запуск ГА
print("\nBest individual: ", ga.best_individual(), "\n") #Вывод лучшей особи популяции (Решение)
for individual in ga.last_generation(): #Вывод всех особей популяции в последнем поколении
  print(individual)