def multiply_lst(lst):
# Задаём условие выхода из рекурсии
    if len(lst) == 0:
        return 1
# Во всех других случаях возвращаем
# сумму первого элемента списка
# и результат суммирования оставшихся
    return lst[0] * multiply_lst(lst[1:])