import pyautogui
import pyperclip
import time
import pandas as pd 

pyautogui.PAUSE = 1

pyautogui.hotkey("win")
pyautogui.write("chrome")
pyautogui.hotkey("enter")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=573, y=430, clicks=2)

time.sleep(2)

pyautogui.click(x=679, y=413)
pyautogui.click(x=1356, y=406)
pyautogui.click(x=1434, y=520)

time.sleep(5)

tabela = pd.read_excel(r"C:\Users\allan\Downloads\Vendas - Dez.xlsx")
print(tabela)

faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()


pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/?hl=pt-BR#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=83, y=216)

time.sleep(2)
pyautogui.write("allandeyvisondi@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")
pyperclip.copy("Relátorio de vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

texto = f"""
Prezados, boa tarde!

O faturamento de ontem foi de: R${faturamento:,.2f}

A quantidade de produtos foi de: {quantidade:,}

Abs 
Allan Deyvison
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")


