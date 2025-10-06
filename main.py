#Романович Никита, 18, 88ТП

list_one = [i for i in range(0,20)] #Генератор списка случайного

list_two = [i**2 for i in list_one] #Генератор списка с квадратами чисел из первого списка

print("Первый список:", end ="")    #Результат
print(list_one)
print("Второй список:", end ="")
print(list_two)