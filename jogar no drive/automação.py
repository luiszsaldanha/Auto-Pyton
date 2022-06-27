
#Abrir o google drive no meu computador
#Entrar ma area de tarbalho
#cliquei no arquivo de backup e arrastei
#Enquanto estou arrastano mudar para o google drive e espearar 5 seg
#Entrei no google drive e soltei o arquivo no drive

import pyautogui
import time

print ('Iniciando...')
print (pyautogui.position())

pyautogui.alert('O código está sendo executado, não mexa em nada.')
pyautogui.PAUSE = 0.7

pyautogui.press('winleft')
pyautogui.write('Opera')
pyautogui.press('enter')

time.sleep(5)
pyautogui.write('https://drive.google.com/drive/u/0/my-drive')
pyautogui.press('enter')

pyautogui.hotkey('winleft', 'd')

pyautogui.moveTo(1315, 45)
pyautogui.mouseDown()
pyautogui.moveTo(628, 511)
pyautogui.hotkey('alt', 'tab')
time.sleep(3)
pyautogui.mouseUp()

pyautogui.alert('O codigo ja acabou, ja pode mexer no computador.')

