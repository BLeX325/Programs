import math

r=[] #создаём пустой список r, который будет содержать все числа псевдослучайной последовательности
r0=0.9147 #инициализируем нулевое r с которого начнётся отсчёт последовательности


def neyman(r0): #функция подсчёта псевдослучайных чисел по методу Неймана
    i=0
    s = ""
    res = r0
    while i < 3: #цикл нахождения псевдослучайных чисел 
        res = (res**2) #возводим r в квадрат
        res = round(res,7) #округляем наше r на 2 последних знака
        s = str(res) #присваеваем переменной s типа str(строка) значение нашего r
        news = s[0]+s[1]+s[4]+s[5]+s[6]+s[7] #теперь из строки с результатом отбрасываем первые две цифры, т.к последние две уже округлены 
        res = float(news) #присваиваем полученное r
        r.append(res) #добавляем полученное значение в список
        i=i+1 #счётчик цикла +1
    return r #возвращаем сформированный из 3-х чисел список


neyman(r0) #вызываем функцию
s = '1) r1 = ' + str(r[0]) + '\n2) r2 = ' + str(r[1]) + '\n3) r3 = ' + str(r[2]) #переменная которая будет выводить конечный результат
print(s) #печатаем конечный результат
