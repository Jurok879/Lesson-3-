def calculate_structure_sum(data_structure):              # создаём функцию для подсчёта данных
    summa = 0                                             # создаем переменную с которой будем работать в теле функции
    if isinstance(data_structure, dict):                  # прописываем условие для словаря
        for key, value in data_structure.items():         # перебираем ключи и значения
            summa += calculate_structure_sum(key)         # суммируем ключи
            summa += calculate_structure_sum(value)       # суммируем значения
    elif isinstance(data_structure, (list, tuple, set)):  # прописываем условие для списка, кортежа и множества
        for item in data_structure:                       # перебираем значения
            summa += calculate_structure_sum(item)        # суммируем значения
    elif isinstance(data_structure, (int, float)):        # прописываем условия дпя целых чисел и с плавающей запятой
        summa += data_structure                           # суммируем значения
    elif isinstance(data_structure, str):                 # прописываем условие для строк
        summa += len(data_structure)                      # суммируем длину строк

    return summa                                          # возврат значения переменной в функцию


data_structure = [                                        # данные из условия задачи
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)                                             # вывод результата функции
