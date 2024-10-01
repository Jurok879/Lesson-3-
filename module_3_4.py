def single_root_words(root_word, *other_words):                              # объявляем функцию

    same_words = []                                                          # создаем пустой список
    for i in other_words:                                                    # с помощью цикла перебираем слова
        if root_word.lower() in i.lower() or i.lower() in root_word.lower(): # прописываем согласно условия
            same_words.append(i)                                             # добавляем слова удовлетворяющие условию
    return same_words                                                        # возвращаем список


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
