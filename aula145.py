import pyautogui
import pyperclip
import time
import pandas as pd

# Configuração da pausa do PyAutoGUI
pyautogui.PAUSE = 1

def abrir_chrome():
    pyautogui.hotkey("win")
    pyautogui.write("chrome")
    pyautogui.hotkey("enter")

def navegar_para_link(link):
    pyperclip.copy(link)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(5)

def fazer_download_do_arquivo():
    pyautogui.doubleClick(x=573, y=430)
    time.sleep(2)
    pyautogui.click(x=679, y=413)
    pyautogui.click(x=1784, y=424)
    pyautogui.click(x=1434, y=520)
    time.sleep(5)

def ler_arquivo_excel(caminho):
    tabela = pd.read_excel(caminho)
    return tabela

def calcular_faturamento_e_quantidade(tabela):
    faturamento = tabela["Valor Final"].sum()
    quantidade = tabela["Quantidade"].sum()
    return faturamento, quantidade

def enviar_email(destinatario, assunto, corpo_email):
    pyautogui.hotkey("ctrl", "t")
    pyperclip.copy("https://mail.google.com/mail/u/0/?hl=pt-BR#inbox")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(x=83, y=216)
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
        nome = input("Qual seu nome? ")
        destinatario = input("Qual e-mail do destinario para enviar o relátorio? ")
        ondeArquivo = input("Caminho do arquivo 'Vendas - Dez': ")
        time.sleep(5)
        abrir_chrome()
        link = "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing"
        navegar_para_link(link)
        fazer_download_do_arquivo()
        caminho_arquivo = f"{ondeArquivo}\Vendas - Dez.xlsx"
        tabela = ler_arquivo_excel(caminho_arquivo)
        faturamento, quantidade = calcular_faturamento_e_quantidade(tabela)
        #destinatario = "allandeyvisondi@gmail.com"
        assunto = "Relatório de vendas"
        corpo_email = f"""
        Prezados, boa tarde!

        O faturamento de ontem foi de: R${faturamento:,.2f}

        A quantidade de produtos foi de: {quantidade:,}

        Abs
         {nome}
        """
        enviar_email(destinatario, assunto, corpo_email)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
