#Проверка на номер игры
def games_number(number):
	if number == '1' or number == '2' : return True
	else : return False
	
#Грамотность
def literacy(chislo):
	if chislo > 4 : return "попыток"
	else : return "попытки"
	
#Проверка на ответ бота
def is_right(c):
	if c == 'да' or c =='больше' or c =='меньше' : return True
	else : return False

#Проверка на решение ты\я
def answer(b):
	if b == 'ты' or b =='я' : return True
	else : return False
	
#Проверка на решение да\нет
def decis(a):
	if a == 'да' or a =='нет' : return True
	else : return False
	
#Проверка на число
def is_number(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

#Проверка интервала на валидность
def is_interval(min,max):
	if min<max : return True
	else : return False
	
#Вычисление кол-ва попыток
def attempts (min, max):
	a = 0
	current = 0
	while True:
		a += 1
		if min == max - 1 : return a + 1
		elif min == max :return a
		else : 
			current = (min + max) // 2
			max = current - 1