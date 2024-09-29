calls = 0                                                        # создаем переменную со значением "0"

def count_calls():                                               # Создаём функцию "count_calls"
    global calls
    calls += 1

def string_info(string):                                         # Создаём функцию "string_info"
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):                         # Создаём функцию "is_contains"
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)


