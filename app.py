from flask import Flask, render_template, jsonify
from selenium import webdriver
from threading import Thread
from django.shortcuts import render
from django.shortcuts import HttpResponse
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from django.http import JsonResponse
import schedule
from flask import Flask, render_template
from flask_socketio import SocketIO
import threading




app = Flask(__name__)

# Função para extrair dados usando Selenium em segundo plano
def extrair_dados():
    # Código para inicializar o driver do Selenium e extrair dados
    # Envie os dados para o frontend (pode usar Flask-SocketIO ou uma API REST)
    def iniciar_driver():

        chrome_options = Options()

        arguments = ['--lang=en-US', '--window-size=1920,1080',
                    '--incognito', '--disable-gpu', '--no-sandbox', '--headless', '--disable-dev-shm-usage']

        for argument in arguments:
            chrome_options.add_argument(argument)
        chrome_options.headless = True
        chrome_options.add_experimental_option('prefs', {
            'download.prompt_for_download': False,
            'profile.default_content_setting_values.notifications': 2,
            'profile.default_content_setting_values.automatic_downloads': 1

        })
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=chrome_options)

        
        return driver
    def digitar_naturalmente(text, elemento):
        for letra in text:
            elemento.send_keys(letra)
            sleep(random.randint(1, 5)/30)
    def extrair_facebook():
        text = "fizzvolibearshen@gmail.com"
        driver = iniciar_driver()
        driver.get('https://www.facebook.com/')
        sleep(3)
        driver.implicitly_wait(12)
        email = driver.find_element(By.ID, "email")
        digitar_naturalmente(text,email)
        driver.implicitly_wait(12)
        password = driver.find_element(By.ID, "pass")
        text = "carateka1000"
        digitar_naturalmente(text,password)
        driver.implicitly_wait(12)
        submit = driver.find_element(By.XPATH, "//button[@class='_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy']")
        submit.click()
        driver.implicitly_wait(20)
        keywords = ["Isaack Amaral"]
        search = driver.find_element(By.XPATH, '//input[@placeholder="Pesquisar no Facebook"]')
        search.click()
        digitar_naturalmente(keywords,search)
        driver.implicitly_wait(20)
        click_search = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div/ul/li[3]/div/a/div/div[2]/span/span")
        click_search.click()

        driver.implicitly_wait(20)
        element = driver.find_element(By.XPATH, "//*[text()='Publicações']")
        element.click()
        driver.implicitly_wait(20)
        max_iteracoes = 10
        iteracao = 0
        cont = 0

        keywords = [
                    "Lying client", "scam alert", "fake reviews", "bad customers",
                    "fraudulent customer", "report", "share experience with clients",
                    "report bad employee", "bad employee", "avoid chargebacks",
                    "avoid scams", "fake refund", "business protection", "web directory"
                ]

                # Lista de frases de resposta
        responses = [
                    "Scammers hurt everyone, report on LC.",
                    "LC exposes them so they can't do it again.",
                    "New scams happen every minute LC has real-time scam alerts.",
                    "I hate that this happened LC was created for this very reason.",
                    "Care to share on LC?",
                    "This is happening far too often post on LC!",
                    "That hurts business growth especially if it isn't true. Write the truth on LC."
                ]

        a = 0
        # Continue fazendo scroll e procurando divs até atingir o limite ou encontrar todas as divs desejadas
        while iteracao < max_iteracoes:
            

            sleep(4)
            comentario_element = driver.find_elements(By.XPATH, "//div[@class='x1i10hfl x1qjc9v5 xjqpnuy xa49m3k xqeqjp1 x2hbi6w x1ypdohk xdl72j9 x2lah0s xe8uvvx x2lwn1j xeuugli x1hl2dhg xggy1nq x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1a2a7pz xjyslct xjbqb8w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1heor9g xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1ja2u2z xt0b8zv']")
            for c in comentario_element:

                comentario_texto = c.text
                print(f"Texto do Comentário: {comentario_texto}")
                c.click()
                sleep(7)
                posicao_inicial = 3

                # Encontre todos os elementos desejados
                todos_os_comentarios = driver.find_elements(By.XPATH, "//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u']")
                sleep(1)

                # Inicialize uma lista vazia para armazenar os textos
                textos = []
                contador = 0
                
                # Itere sobre os elementos a partir da posição inicial
                for elemento in todos_os_comentarios[posicao_inicial:]:
                    textos.append(elemento.text)
                    nova_variavel = textos.copy()
                    socketio.emit('dados_atualizados', {'dados': nova_variavel})
                    sleep(5)
                    contando = 0

                    sleep(2)
                
                exits = driver.find_element(By.XPATH, "//div[@class='x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 x14yjl9h xudhj91 x18nykt9 xww2gxu x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x78zum5 xl56j7k xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 xc9qbxq x14qfxbe x1qhmfi1']")

                exits.click()
                sleep(6)
                action = ActionChains(driver)
                for _ in range(9):
                    action.send_keys(Keys.DOWN).perform()
                sleep(2)
                cont+=1
                if c == len(comentario_element):
                # Se sim, definir contando de volta para 0
                    for _ in range(25):
                        action.send_keys(Keys.DOWN).perform()
                    sleep(2)
                    c = 0

            
            cont += 1

            # Role para baixo para carregar mais divs
            sleep(3)  # Aguarde o carregamento das novas divs

            iteracao += 1
        print(cont)
        sleep(20)
    extrair_facebook()

@app.route('/')
def index():
    return render_template('index.html')

# Rota para obter dados do frontend
@app.route('/api/dados', methods=['GET'])
def obter_dados():
    # Lógica para obter os dados extraídos e enviá-los para o frontend
    dados = {'mensagem': 'Dados extraídos do site'}
    return jsonify(dados)

# Inicie o processo de extração de dados em segundo plano
def iniciar_extracao():
    while True:
        extrair_dados()

socketio = SocketIO(app)
if __name__ == '__main__':
    # Inicie a thread para a extração em segundo plano
    thread = threading.Thread(target=extrair_dados)
    thread.start()

    # Inicie o servidor Flask-SocketIO
    socketio.run(app, debug=True)
