# List - Списък - Mutable - Могат да бъдат променяни
list = []
print(list) # immutable operation

list.append(1) # mutable operation # Добавяне на стойност на списъка
list.insert(0,-1) # mutable operation # Добавяне на стойност на някакъв индекс

print(list[0]) # immutable operation  # Принтиране на стойност на някакъв индекс

list.pop() # mutable operation # Премахване на елементи

# Tuple - Immutable - Не могат да бъдат променяни
tuple = ()

tuple = (1, 2, 3, 4)
print(tuple)    # immutable operation
print(tuple[0]) # immutable operation
tuple = (1,2,3) # overwrites the value of tuple

# single element tuple list/tuple - създаване на тюпъл с 1 елемент
list2 = [1]
print(list2) # [1]

tuple2 = (1)
print(tuple2) # 1 - Получава се стойност без никакви скоби при tuple по време на принтирането

# Празен tuple
()




