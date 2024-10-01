def get_multiplied_digits(number):                                 # создаем функцию
    str_number = str(number)                                       # создаем переменную со строковым значением
    first = int(str_number[0])                                     # создаем переменную с числовым значением
    if len(str_number) > 1:                                        # условие, согласно условию задачи
        return first * get_multiplied_digits(int(str_number[1:]))  # возвращаем значения
    else:
        return first




result = get_multiplied_digits(40203)
print(result)
