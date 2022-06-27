#abrir navegador(opera)
#pesquisar gmail
#abrir gmail
#clicar na aba que deseja apagar (promotions, social, main)
#pegar os mais velhos (oldest)
#caixinha com seta -> all
#clica na caixa
#lixeira
#newer
#return tudo 
#pyautogui.press("")
#pyautogui.write("")
#
#

from pydoc import cli
import pyautogui
import time

print ('Iniciando...')

pyautogui .alert('O codigo vai começar, não mexa em nada.')
pyautogui.PAUSE = 0.5

pyautogui.press("winleft")
pyautogui.write("opera")
pyautogui.press("enter")

time.sleep(2)

pyautogui.write("https://mail.google.com/mail/u/0/#inbox")

time.sleep(2)
#gmail
pyautogui.press("enter")

time.sleep(10)

#open email
pyautogui.moveTo(709, 204)
pyautogui.click()

#click on oldest
pyautogui.moveTo(1192, 155)
pyautogui.click()

#oldest
pyautogui.moveTo(1148, 233)
pyautogui.click()

time.sleep(6)

#newer
pyautogui.moveTo(1229, 159)
#time.sleep(3)
pyautogui.click() 

time.sleep(6)

#arrow checkbox
pyautogui.moveTo(157,156) 
pyautogui.click()

#all
pyautogui.moveTo(160, 190)
pyautogui.click() 

#trash
pyautogui.moveTo(274, 160)
pyautogui.click()

#criar um loop


print('Acabou')





