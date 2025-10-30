import pyautogui
import time
import datetime

date_hoje = datetime.datetime.now().strftime("%d.%m.%Y")
date = f"inadimplente_0460_{date_hoje}"


## pyautogui.PAUSE(3)
## >>> especie de time.sleep global 

pyautogui.click(x=1917, y=1057)
# fecha vscode
pyautogui.click(x=884, y=41, clicks=2)
# abre o PBI
time.sleep(40)

pyautogui.click(x=530, y=1007)
# nas tabelas abaixo seleciona "Aging Operação"

pyautogui.moveTo(x=757 , y=109, duration=1)
# simula click de atualização da BD

time.sleep(5)
# espera da atualização

pyautogui.click(x=179, y=628)
# seleciona o aging de - 04 à 60 dias

pyautogui.moveTo(x=1384, y=320)
time.sleep(2)
# exportar dados + espera pop up

pyautogui.click(x=1473, y=323, duration=1)
pyautogui.click(x=1500, y=341, duration=1)
# exportar dados 


pyautogui.moveTo(x=767, y=544, duration=1)

pyautogui.click(x=752, y=502)
# area de trabalho


pyautogui.click(x=944, y=788, duration=1)
# seleciona campo de nomeação de arquivo

pyautogui.write(date)
time.sleep(1)
pyautogui.click(x=1466, y=856)
# salva