#tem que instalar tais bibliotecas
import pyautogui
import requests
import schedule
import time
from datetime import datetime
 
def capturar_cotacao():
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    if response.status_code == 200:
        dados = response.json()
        cotacao = dados['rates']['BRL']
 
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
        texto_cotacao = f"Cotação do dólar em {data_hora}: R${cotacao:.2f}"
 
        pyautogui.hotkey('win', 'r')
        pyautogui.sleep(1)
        pyautogui.write('notepad')
        pyautogui.press('enter')
        pyautogui.sleep(2)
 
        pyautogui.write(texto_cotacao)
        pyautogui.press('enter')
 
        pyautogui.hotkey('ctrl', 's')
        pyautogui.sleep(1)
 
        nome_arquivo = f"cotacao_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
        pyautogui.write(nome_arquivo)
        pyautogui.press('enter')
 
        pyautogui.sleep(1)
        pyautogui.hotkey('alt', 'f4')
 
 
print("Programa de monitoramento de cotação iniciado!")
print("Pressione Ctrl+C para encerrar")
schedule.every(10).seconds.do(capturar_cotacao)
 
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("Programa encerrado pelo usuário")