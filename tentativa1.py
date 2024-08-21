import pyautogui
import pyperclip
import time
import pandas as pd

# Configuração da pausa do PyAutoGUI
pyautogui.PAUSE = 1

def click(image_path):
    try:
        x, y = pyautogui.locateCenterOnScreen(image_path)
        pyautogui.click(x,y)
    except TypeError:
        print("Elemento não encontrado na tela.")

def doubleClick(image_path):
    try:
        x, y = pyautogui.locateCenterOnScreen(image_path)
        pyautogui.doubleClick(x,y)
    except TypeError:
        print("Elemento não encontrado na tela.")

def rightClick(image_path):
    try:
        x, y = pyautogui.locateCenterOnScreen(image_path)
        pyautogui.click(x, y, button='right')
    except TypeError:
        print("Elemento não encontrado na tela.")

def abrir_chrome():
    pyautogui.hotkey("win")
    pyautogui.write("chrome")
    pyautogui.hotkey("enter")

def navegar_para_link(link):
    pyperclip.copy(link)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(5)

def fazer_download_do_arquivo(arquivoImg1, arquivoImg2,img12):
    #pyautogui.doubleClick(x=573, y=430)
    doubleClick(arquivoImg1)
    time.sleep(2)
    #click(arquivoImg2)
    click(img12)
    #click(arquivoImg3)
    #pyautogui.click(x=679, y=413)
    #pyautogui.click(x=1356, y=406)
    #pyautogui.click(x=1434, y=520)
    time.sleep(5)

def ler_arquivo_excel(caminho):
    tabela = pd.read_excel(caminho)
    return tabela

def calcular_faturamento_e_quantidade(tabela):
    faturamento = tabela["Valor Final"].sum()
    quantidade = tabela["Quantidade"].sum()
    return faturamento, quantidade

def enviar_email(destinatario, assunto, corpo_email, arquivoImg4):
    pyautogui.hotkey("ctrl", "t")
    pyperclip.copy("https://mail.google.com/mail/u/0/?hl=pt-BR#inbox")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(2)
    #pyautogui.click(x=83, y=216)
    doubleClick(arquivoImg4)
    time.sleep(2)
    pyautogui.write(destinatario)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyperclip.copy(assunto)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("tab")
    pyperclip.copy(corpo_email)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("ctrl", "enter")




#trocar o caminho do arquivo para o seu diretorio
#colocar seu o seu e-mail destinario 
def main():
    try:
        #nome = input("Qual seu nome? ")
        #destinatario = input("Qual e-mail do destinario para enviar o relátorio? ")
        abrir_chrome()
        link = "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing"
        navegar_para_link(link)
        #fazer_download_do_arquivo()
        arquivoImg1 = r"C:\Users\allan\Documents\facu\Primeiro Simestre\Algoritimos e Lógica de Programação\cursopython\trabalho\imgclick\exportar.png"
        arquivoImg2 = r"C:\Users\allan\Documents\facu\Primeiro Simestre\Algoritimos e Lógica de Programação\cursopython\trabalho\imgclick\arquivo.png"
        #arquivoImg3 = r"C:\Users\allan\Documents\facu\Primeiro Simestre\Algoritimos e Lógica de Programação\cursopython\trabalho\imgclick\download.png"
        arquivoImg4 = r"C:\Users\allan\Documents\facu\Primeiro Simestre\Algoritimos e Lógica de Programação\cursopython\trabalho\imgclick\escrever.png"
        img12 = r"C:\Users\allan\Documents\facu\Primeiro Simestre\Algoritimos e Lógica de Programação\cursopython\trabalho\imgclick\down.png"
        fazer_download_do_arquivo(arquivoImg1, arquivoImg2, img12 )
        caminho_arquivo = r"C:\Users\allan\Downloads\Vendas - Dez.xlsx"
        tabela = ler_arquivo_excel(caminho_arquivo)
        faturamento, quantidade = calcular_faturamento_e_quantidade(tabela)
        destinatario = "allandeyvisondi@gmail.com"
        assunto = "Relatório de vendas"
        corpo_email = f"""
        Prezados, boa tarde!

        O faturamento de ontem foi de: R${faturamento:,.2f}

        A quantidade de produtos foi de: {quantidade:,}

        https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing

        Abs


        """
        enviar_email(destinatario, assunto, corpo_email, arquivoImg4)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
