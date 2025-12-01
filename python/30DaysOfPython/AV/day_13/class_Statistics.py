"""class Statistics:
    def __init__(self, list_of_data:list):
        self.list_of_data = list_of_data
        
    #Methods
    def count(self):
        return self.list_of_data.count()
    def sum(self):
        list_of_data = self.list_of_data
        return sum(list_of_data)
    def min(self):
        list_of_data = self.list_of_data
        return min(list_of_data)
    def max(self):
        list_of_data = self.list_of_data
        return max(list_of_data)
    def range(self):
        list_of_data = self.list_of_data
        return max(list_of_data) - min(list_of_data)
    def mean(self):
        list_of_data = self.list_of_data
        return round(sum(list_of_data) / len(list_of_data))
    def median(self):
        list_of_data = self.list_of_data
        list_of_data.sort()
        if len(list_of_data) %2 == 0:
            median_index = (len(list_of_data) - 1)//2
            median = (list_of_data[median_index] + list_of_data[median_index+1])//2
            return median
        if True:
            median_index = (len(list_of_data) - 1)//2
            return list_of_data[median_index]
    def mode(self):
        list_of_data = self.list_of_data
        # Crear un diccionario vacío para almacenar los conteos
        frecuencias = {}

        # Contar la frecuencia de cada número en la lista
        for numero in list_of_data:
            if numero in frecuencias:
                frecuencias[numero] += 1
            else:
                frecuencias[numero] = 1

        # Si la lista está vacía, no hay moda
        if not frecuencias:
            return []

        # Encontrar la frecuencia más alta
        max_frecuencia = 0
        for frecuencia in frecuencias.values():
            if frecuencia > max_frecuencia:
                max_frecuencia = frecuencia

        # Encontrar todos los números con la frecuencia más alta
        modas = []
        for numero, frecuencia in frecuencias.items():
            if frecuencia == max_frecuencia:
                modas.append(numero)

        # Devolver la lista de modas
        return modas   
    def var(self):
        list_of_data = self.list_of_data
        median = Statistics.median(self)    
        list_aux= []
    
        for number in list_of_data:
            list_aux.append((number - median)**2)
    
        return sum(list_aux)/len(list_aux)
    def std(self):
        from math import sqrt
        variance = Statistics.var()

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)        
print("Variance:", data.var())"""

"""
class Usuario:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def sign_in(self):
        print(f"El usuario {self.name} ha iniciado sesion")
            
usuario1 = Usuario("Alejandro", "Vera")

usuario1.sign_in()
"""

class Square:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        
    def print_square(self):
        print("* " * self.weight)
        for lado in range(self.height-2):
            
            print(f"*{'  '*(self.weight - 1)}*")
            
        print("* " * (self.weight))        
            

            
small_square = Square(3, 6)

small_square.print_square()           
                                                