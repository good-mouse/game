#Реализовать компьютерную версию игры в города.
# Вы называете город, компьютер отвечает,
# затем опять вы. Компьютер должен следить за
# соблюдением правил, а также за тем, чтобы не было повторов городов.
 
#Импоритуем всё необходимое
from random import choice #импоритуем функцию из модуля random
import os
import verification

#Импортируем базу городов
f=open("goroda_base.txt","r+")
s=(f.read())
goroda=s.split('\n')
f.close()

goroda_copy=goroda.copy() #делаем рабочий список городов, из которогу будем удалять значения
 
#Проверка на правильное слово
def check_word(word1,word2):
	a = word1[len(word1)-1]
	b = word2[0]
	if a == b.lower(): return True
	else: return False
# функция возврата первой буквы
def first_letter(word):
    first_letter=word[0]
    return first_letter
 
# функция возврата последней буквы, если последняя буква 'ь'-'й'-'ы', то берём предпоследнюю
def end_letter(word):
    end_letter=word[len(word)-1]
    if end_letter=='ь' or end_letter=='й' or end_letter=='ы':
        end_letter=word[len(word)-2]
    return end_letter
 
#возвращает случайный город из списка - первый ход компьютера
def first_turn_comp():
    return choice(goroda)
 
# Ход компьютера: функция принимает в качестве аргумента город который вводит пользователь,
# проходит по базе данных городов и формирует список городов, которые начинаются с последней буквы города пользователя
# затем возвращает случайный город из этого списка.
# Удаляет города которые уже были.
def computer_turn(turn_player):
    first_letter_tc=end_letter(turn_player)  #Первая буква города компа = последней букве города игрока
    goroda_copy.remove(turn_player)          #Удаляем город который назвал пользователь
    list=[]
    for i in goroda_copy:          #формирует список городов, которые начинаются с последней буквы города пользователя
        if first_letter_tc.upper()==first_letter(i):
            list.append(i)
    choice_comp=choice(list)                 #Город который выбркал комп из подготовленного списка
    goroda_copy.remove(choice_comp)          #Удаляем город который назвал компьютер
    return choice_comp                       #Возвращаем город который выбркал комп из подготовленного списка
	
def game():
	print("Ну чтож давай поиграем в игру \nПравила простые, я называю город, а ты должен назвать город, начинающийся на последнюю букву моего города\nПиши города с БОЛЬШОЙ буквы, иначе я тебя не пойму\nЕсли последняя буква города ь, й или ы, то называй город на предыдущюю букву.\nИграть будем пока ты не скажешь стоп\nЕсли готов начать нажми Enter")
	input()
	os.system('cls')
	# Первый ход компьютера и игрока
	turn_comp = first_turn_comp()
	print("Мой город: " + turn_comp)
	while True:
		turn_player = str(input("Твой город: "))
		check = check_word(turn_comp,turn_player)
		if check == True : break
		else: 
			print("Не по правилам, введи город на букву " + (turn_comp[len(turn_comp)-1]).upper())
			continue
	
	# Последующие ходы игрока и компа
	stop = ''
	while True:
		if turn_player in goroda_copy:
			turn_comp = computer_turn(turn_player)
			print("Мой город: " + turn_comp)
			while True:
				turn_player = str(input("Твой город: "))
				check = check_word(turn_comp,turn_player)
				if check == True : break
				else: 
					print("Не по правилам, введи город на букву " + (turn_comp[len(turn_comp)-1]).upper())
					continue
			
		else:
			if turn_player not in goroda:# Проверяем существует вообще город который ввёл игрок или нет
				if turn_player == 'стоп': 
					os.system('cls')
					stop = turn_player
					return
				print("Такого города вообще не существует")
				while True:
					turn_player = str(input("Твой город: "))
					if turn_player == 'стоп': 
						os.system('cls')
						stop = turn_player
						return
					check = check_word(turn_comp,turn_player)
					if check == True : break
					else: 
						print("Не по правилам, введи город на букву " + (turn_comp[len(turn_comp)-1]).upper())
						continue
			else:
				print("Такой город уже был")
				while True:
					turn_player = str(input("Твой город: "))
					if turn_player == 'стоп': 
						os.system('cls')
						stop = turn_player
						return
					check = check_word(turn_comp,turn_player)
					if check == True : break
					else: 
						print("Не по правилам, введи город на букву " + (turn_comp[len(turn_comp)-1]).upper())
						continue
