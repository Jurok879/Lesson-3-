# 1. Функция с параметрами по умолчанию:

def print_params(a=1, b='строка', c=True):       # создаем функцию со значениями по умолчанию
    print(a, b, c)
print_params()

def print_params():                              # создаем функцию без аргументов
    print()
print_params()

def print_params(b=25):                          # создаем функцию со значением "b"
    print(b)
print_params()

def print_params(c=[1, 2, 3]):                   # создаем функцию со значением "c"
    print(c)
print_params()

# 2. Распаковка параметров:

values_list = [5, 'бревно', False]
values_dict = {'a': 10, 'b': 'пень', 'c': True }

def print_params(*values_list):
    print(values_list)
print_params(*values_list)                       # распаковка с помощью "*" для списка

def print_params(**values_dict):
    print(values_dict)
print_params(**values_dict)                      # распаковка с помощью "**" для словаря

#3. Распвковка + отдельные параметры:

value_list_2 = [54.32, 'Строка']

def print_params(*value_list_2):
    print(' '.join(map(str, value_list_2)))
print_params(*value_list_2, 42)                  # распаковка с отдельными параметрами


