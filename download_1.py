import pyautogui as P
import os
from time import sleep
import keyboard

caminho_site = os.path.abspath("site.jpg")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
caminho_xml = os.path.abspath("xml.jpg")
caminho_robo = os.path.abspath("robo.jpg")
caminho_robo_verde = os.path.abspath("verde.jpg")
caminho_down = os.path.abspath("down.jpg")
caminho_ok = os.path.abspath("ok.jpg")
caminho_salvar = os.path.abspath("salvar.jpg")



def clicar_site(importe, tentativas=200):
    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(importe, confidence=0.9)
            if posicao is not None:
                centro_x, centro_y = P.center(posicao)
                P.click(centro_x, centro_y)
                break
            else:
                print(f"...")
        except Exception as e:
            print(f"Procurando_clicar_site{e}")
    else:
        raise Exception(f"Erro {tentativas} tentativas.")
       
def clicar_xml(importe, tentativas=200):
    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(importe, confidence=0.9)
            if posicao is not None:
                centro_x, centro_y = P.center(posicao)
                P.click(centro_x, centro_y)
                P.write(linha)
                break
            else:               
                print(f"...")
        except Exception as e:
            print(f"Procurando_clicar_xml( {e}")
    else:
        raise Exception(f"Erro {tentativas} tentativas.")

def clicar_robo(importe, tentativas=200):
    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(importe, confidence=0.9)
            if posicao is not None:
                centro_x, centro_y = P.center(posicao)
                P.click(centro_x, centro_y)
                break
            else:               
                print(f"...")
        except Exception as e:
            print(f"Procurando_clicar_robo{e}")
    else:
        raise Exception(f"Erro {tentativas} tentativas.")

def clicar_robo_verde(importe, tentativas=200):
    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(importe, confidence=0.9)
            if posicao is not None:
                centro_x, centro_y = P.center(posicao)
                P.click(centro_x, centro_y)
                break
            else:               
                print(f"...")
        except Exception as e:
            print(f"Procurando_clicar_robo_verde {e}")
    else:
        raise Exception(f"Erro {tentativas} tentativas.")

def clicar_robo_verde(importe, tentativas=200):
    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(importe, confidence=0.9)
            if posicao is not None:
                centro_x, centro_y = P.center(posicao)
                P.click(centro_x, centro_y)
                sleep(1)
                #Clicar confirmar
                for _ in range(5):
                    P.press('tab')
                    sleep(0.2)
                P.press('enter')
                break
            else:               
                print(f"...")
        except Exception as e:
            print(f"Procurando_clicar_robo_verde {e}")
    else:
        raise Exception(f"Erro {tentativas} tentativas.")

def clicar_down(importe, tentativas=200):
    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(importe, confidence=0.9)
            if posicao is not None:
                centro_x, centro_y = P.center(posicao)
                P.click(centro_x, centro_y)
                break
            else:               
                print(f"...")
        except Exception as e:
            print(f"Procurando_clicar_down {e}")
    else:
        raise Exception(f"Erro {tentativas} tentativas.")

def clicar_ok(importe, tentativas=200):
    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(importe, confidence=0.9)
            if posicao is not None:
                centro_x, centro_y = P.center(posicao)
                P.click(centro_x, centro_y)
                P.press('enter')
                break
            else:               
                print(f"...")
        except Exception as e:
            print(f"Procurando_clicar_okn {e}")
    else:
        raise Exception(f"Erro {tentativas} tentativas.")
    
def clicar_salvar(importe, tentativas=200):
    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(importe, confidence=0.9)
            if posicao is not None:
                centro_x, centro_y = P.center(posicao)
                P.click(centro_x, centro_y)
                break
            else:               
                print(f"...")
        except Exception as e:
            print(f"Procurando_clicar_salvar {e}")
    else:
        raise Exception(f"Erro {tentativas} tentativas.")

# Abrir o arquivo 'texto.txt' e ler cada linha
with open('texto.txt', 'r') as arquivo:
    for linha in arquivo:
        # Remover espaços em branco no início e no final da linha
        linha = linha.strip()
        
        try:
            clicar_site(caminho_site)
            clicar_xml(caminho_xml)
            clicar_robo(caminho_robo)
            clicar_robo_verde(caminho_robo_verde)
            clicar_down(caminho_down)
            clicar_ok(caminho_ok)
            clicar_salvar(caminho_salvar)
        except Exception as e:
            print(f"Erro geral: {e}")    