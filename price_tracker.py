#𝑭𝒆𝒊𝒕𝒐 𝒑𝒐𝒓 𝑽𝒊𝒏𝒊𝒄𝒊𝒖𝒔 𝑺𝒂𝒏𝒕𝒐𝒔-𝑻𝒆𝒄𝒉
#𝑴𝒐𝒏𝒊𝒕𝒐𝒓𝒂𝒎𝒆𝒏𝒕𝒐 𝒅𝒆 𝑷𝒓𝒆𝒄̧𝒐𝒔 - 𝑰𝑷𝑯𝑶𝑵𝑬 16-𝒆

import requests
import pandas as pd
from bs4 import BeautifulSoup
import time


def Relatorio():

    print("----TABELA COM PREÇOS DE IPHONES----")
    time.sleep(0.5)
    while True:
        print("⏱️Gerando Relatorio...")
        time.sleep(2)
        print("💵------IPHONE-16E------💵")

        dados = [
            ['▶LOJA◀', '▶PREÇOS◀'],
            ['AMAZON', Preço1()],
            ['ZOOM', Preço2()], 
            ['CARREFOUR', Preço3()],
            ['BUSCAPE', Preço4()],
            ['LIVELO', Preço5()],
        ]

        tabela = pd.DataFrame(dados)
        print(tabela)
        print("------------")
        print("⏱︎Proximo Relatorio À 6 Horas...⏱︎")
        time.sleep(21600)

def Preço1():
    #LOJA AMAZON
    global Loja1
    Loja1 = 'AMAZON'
    global VPreço1
    url1 = 'https://www.amazon.com.br/Smartphone-Samsung-Galaxy-C%C3%A2mera-Recursos/dp/B0DYVMWMNM/ref=asc_df_B0DYVMWMNM?mcid=fb95d6a7da5c368ebb4a0ff4e9bc6cd5&tag=googleshopp00-20&linkCode=df0&hvadid=709964503151&hvpos=&hvnetw=g&hvrand=2347465545261026696&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9100965&hvtargid=pla-2448309485204&language=pt_BR&gad_source=1&th=1'

    response = requests.get(url1)
    dado = response.json
    soup = BeautifulSoup(response.text,'html.parser')
    todo_texto = soup.get_text()
    if "R$" in todo_texto:
        posiçao = todo_texto.find("R$")
        VPreço1 = todo_texto[posiçao:posiçao+10]
        return VPreço1
    else:
        print("Preço nao encontrado")
def Preço2():
    #LOJA ZOOM
    global Loja2
    Loja2 = 'ZOOM'
    global VPreço2
    url2 = 'https://www.zoom.com.br/celular/smartphone-apple-iphone-16-128gb-camera-dupla?og=18000&gad_source=1&gad_campaignid=23017617316&gbraid=0AAAAADlBCe7GxkVylcqwGHu_zt-b8-wSx&gclid=CjwKCAjwx-zHBhBhEiwA7Kjq62g8ksFm9JZ_9ekChWNm9h62e-hLOiJYczVESlT1N_AotrYxnCGhvhoCCiYQAvD_BwE'
    response = requests.get(url2)
    soup = BeautifulSoup(response.text, 'html.parser')
    todo_texto = soup.get_text()
    if "R$" in todo_texto:
        posiçao = todo_texto.find("R$")
        VPreço2 = todo_texto[posiçao:posiçao+ 11]
        return VPreço2
    else:
        print("nao encontrado")


def Preço3():
    #Carrefour
    global Loja3
    Loja3 = 'CARREFOUR'
    url3 = 'https://www.carrefour.com.br/apple-iphone-16e-de-128gb-tecnologia-5g-mp951194184/p?utm_medium=sem&utm_source=google_pmax_3p&utm_campaign=3p_performancemax_Eletro_Apostas3p&gad_source=1&gad_campaignid=21012471034&gbraid=0AAAAADjinolo-4cHBQ6uYWmNV1FXT0Fbw&gclid=CjwKCAjwx-zHBhBhEiwA7Kjq6-Scf8LxSgV2hk0V_yAg4iRtgjk56k6jO-aRCEeP1umG-QV1pT_-lBoC4LIQAvD_BwE'
    response = requests.get(url3)
    soup = BeautifulSoup(response.text, 'html.parser')

    texto_todo = soup.get_text()
    if "R$" in texto_todo:
        posiçao = texto_todo.find("R$")
        VPreço3 = texto_todo[posiçao:posiçao+11]
        return VPreço3
    else:
        print("Nao encontrado")

def Preço4():
    #LOJA BUSCAPE
    global Loja4
    Loja4 = 'BUSCAPE'
    
    url4 = 'https://www.buscape.com.br/offer?oid=1453934288&sortorder=-1&pagesize=-1&feed_only_mkp=true&pla=2025-10-24T21:49:48.309213508&og=19221&gad_source=1&gad_campaignid=22735399328&gbraid=0AAAAAD-OhXbNIICmsFATvsM8l5fMFxmmt&gclid=CjwKCAjwx-zHBhBhEiwA7Kjq6weYg4wVRYotcFdpE38qrqdFJEhZt_G95-TiFZWpeqSFPjqfzZUGUBoCuh4QAvD_BwE'
    response = requests.get(url4)
    soup = BeautifulSoup(response.text, 'html.parser')
    todo_texto = soup.get_text()
    if "R$" in todo_texto:
        Find = todo_texto.find("R$")
        VPreço4 = todo_texto[Find:Find+11]
        return VPreço4
    else:
        VPreço4 = print("Not Found")

def Preço5():
    #LOJA LIVELO
    
    global Loja5
    Loja5 = 'LIVELO' 
    
    url5 = 'https://www.livelo.com.br/shopping/apple-iphone-16e-de-128gb-branco/produto/PRD3987447?skuId=SKU4946730&gad_source=1&gad_campaignid=21895551570&gbraid=0AAAAAC73hNXP_C4xkmZ3Q7K0kIxfhMznb&gclid=CjwKCAjwx-zHBhBhEiwA7Kjq6_wTulX_zEl-37kF5FEx9qEV0IXeKr1ZYDqmsybDLHQtIcS2dcy9fRoCVc8QAvD_BwE'
    response = requests.get(url5)
    soup = BeautifulSoup(response.text, 'html.parser')

    texto_todo = soup.get_text()
    if "R$" in texto_todo:
        posiçao = texto_todo.find("R$")
        VPreço5 = texto_todo[posiçao:posiçao+11]
        return VPreço5
    else:
        print("Nao encontrado")

#=============================================================
Opçao = input("Aperte uma Tecla para iniciar!")
Relatorio()
