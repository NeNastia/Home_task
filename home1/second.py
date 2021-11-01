#Задача 2
N = input("Ввести строку,в котрой упоминается Дядя Стёпа: \n") #текст статьи

new_text = N.replace("Uncle Styopa", "Mishka").replace("Uncle", "Mishka").replace("Styopa", "Mishka") #замена имен
#ответ:
print(new_text)