import pyautogui
import time 
import datetime

data_hoje = datetime.datetime.now().strftime("%d.%m.%Y")
data = f"inadimplente_0460_{data_hoje}"

pyautogui.write(data)