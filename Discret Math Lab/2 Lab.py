import heapq #подключаем класс для создания очереди с приоритетом
from collections import Counter, namedtuple #подключаем класс Counter который будет поддерживать счётчик того сколько раз элемент повторился
#функция namedtuple помогает более компактно создавать классы

class Node(namedtuple("Node", ["left","right"])): #ласс внутреннего узла дерева
    def walk(self, code, acc): #обход дерева для узлов
        self.left.walk(code, acc + "0") #спускаемся к левому потомку, добавляя префикс 0
        self.right.walk(code, acc + "1")#спускаемся к правому потомку, добавляя префикс 1
        
class Leaf(namedtuple("Leaf", ["char"])):#лист нашего дерева
    def walk(self, code, acc): #обход дерева для листа
        code[self.char] = acc or "0" #записываем в словарь код построенный код данного символа

def huffman_encode(s): #фукнция которая кодирует некоторую строку символов
    h = [] 
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))#добавляем в список h информацию о каждом элементе
        
    heapq.heapify(h) #строим очередь с приоритетами

    count = len(h)
    while len(h) > 1: #пока в очереди есть хотя бы 2 элемента
        freq1, _count1, right = heapq.heappop(h) #достаём эл-т с мин. частотой 
        freq2, _count2, left = heapq.heappop(h) #следующий за ним эл-т с мин. частотой
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right))) #добавляем новый эл-т, у кот-го частота равна сумме частот предыдущих эл-тов, а так же обозначаем новый узел его потомков
        count += 1 

    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "") #обходим полученное дерево с корня и заполняем словарь code
    return code

def huffman_decode(en, code): #функция которая получает код Хаффмана и декодирует его в строку символов
    pointer = 0 #счётчик
    encoded_str = '' #строка для ответа
    while pointer < len(en): #пока счётчик меньше чем кол-во символов кода
        for ch in code.keys(): #для каждой буквы в коде
            if en.startswith(code[ch], pointer): #если часть закодированной строки совпадает с кодом буквы
                encoded_str += ch #добавляем в выходную строку раскодированную букву
                pointer += len(code[ch]) #к счётчику добавляем кол-во символов сообщения которые мы раскодировали
    return encoded_str #возвращаем полученную строку с буквами

def encode_word(word,code): #функция раскодирования слова
    i = 0 #счётчик сколько символов пройдено
    w = ""
    while i < len(word): #пока счётчик кол-ва символов меньше чем длина полученной строки
        for ch in code: #для каждой буквы в коде
            if word[i] == ch: #если буква полученной строки совпадает с буквой из кода
                w = w + code[ch] #записываем в выходную строку код этой буквы
        i = i + 1 #переходим к следующей букве строки
    return 'Слово "' + str(word)+ '" в коде Хаффмана: ' + w #возвращаем закодированное слово

def main(): #главная функция
    print("Задача 33:") #печатаем заголовок первой задачи
    s = str("а"*16)+str("н"*8)+str("о"*24)+str("е"*27)+str("т"*9)+str("и"*16)#вводим данные в задачи буквы, частоту обозначая как кол-во раз которе буквы встретятся в строке
    code = huffman_encode(s) #присваиваем переменной code результат работы функции закодирования Хаффмана
    for ch in code: #для каждой буквы в таблице кода
        print("{}: {}".format(ch, code[ch])) #печатаем букву и её код

    wd = "тина" #вводим слово которое нужно закодировать в задачи 34
    print("\nЗадача 34:",encode_word(wd,code))#печатаем результат задачи 34
    print("\nЗадача 35:", huffman_decode("0101100110",code))#печатаем результат задачи 35

main() #вызываем нашу главную функцию


