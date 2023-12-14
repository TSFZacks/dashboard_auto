from django.shortcuts import render
from django.shortcuts import HttpResponse
from selenium import webdriver
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

def index(request):
    return render(request, 'pages/index.html')
def facebook_views(request):
    return render(request, 'pages/facebook_page.html')
def botao_facebook(request):
    
    def time_schedule():
        def iniciar_driver():
            chrome_options = Options()
            arguments = ['--lang=pt-BR', '--incognito']
            for argument in arguments:
                chrome_options.add_argument(argument)

            chrome_options.add_experimental_option('prefs', {
                'download.prompt_for_download': False,
                'profile.default_content_setting_values.notifications': 2,
                'profile.default_content_setting_values.automatic_downloads': 1,

            })
            driver = webdriver.Chrome(service=ChromeService(
                ChromeDriverManager().install()), options=chrome_options)

            return driver

        def digitar_naturalmente(text, elemento):
            for letra in text:
                elemento.send_keys(letra)
                sleep(random.randint(1, 5)/30)

        text = "fizzvolibearshen@gmail.com"
        driver = iniciar_driver()
        driver.get('https://www.facebook.com/')
        sleep(3)
        driver.maximize_window()
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
        keywords = ["Lying client"]
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
        # Continue fazendo scroll e procurando divs até atingir o limite ou encontrar todas as divs desejadas
        while iteracao < max_iteracoes:
            divs = driver.find_elements(By.XPATH, "//div[@class='x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z']")
            cont = 0
            for div in divs:
                try:
                    driver.implicitly_wait(20)
                    comentario_element = div.find_element(By.XPATH, ".//span[contains(text(), 'comentário')]")
                    comentario_texto = comentario_element.text
                    print(f"Texto do Comentário: {comentario_texto}")
                    comentario_element.click()
                    sleep(20)
                    posicao_inicial = 3

                    # Encontre todos os elementos desejados
                    elementos = driver.find_elements(By.XPATH, "//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u']")

                    # Inicialize uma lista vazia para armazenar os textos
                    textos = []

                    # Itere sobre os elementos a partir da posição inicial
                    for elemento in elementos[posicao_inicial:]:
                        textos.append(elemento.text)

                    # Agora, 'textos' contém os textos dos elementos a partir da posição [3]
                    print(textos)
                    sleep(2)
                    
                    exits = driver.find_element(By.XPATH, "//div[@class='x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 x14yjl9h xudhj91 x18nykt9 xww2gxu x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x78zum5 xl56j7k xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 xc9qbxq x14qfxbe x1qhmfi1']")

                    exits.click()
                    sleep(6)
                    action = ActionChains(driver)
                    for _ in range(16):
                        action.send_keys(Keys.DOWN).perform()
                    sleep(2)
                    cont+=1

                except:
                    print("Campo de comentário não encontrado nesta div.")
                    action = ActionChains(driver)
                    for _ in range(16):
                        action.send_keys(Keys.DOWN).perform()
                    sleep(2)
                cont += 1

            # Role para baixo para carregar mais divs
            sleep(3)  # Aguarde o carregamento das novas divs

            iteracao += 1
        print(cont)
        return JsonResponse({'textos': textos})
    schedule.every(2).days.do(time_schedule)
    while True:
        schedule.run_pending()
        sleep(1)

def face_coments(request):
    def iniciar_driver():
            chrome_options = Options()
            arguments = ['--lang=pt-BR', '--incognito']
            for argument in arguments:
                chrome_options.add_argument(argument)

            chrome_options.add_experimental_option('prefs', {
                'download.prompt_for_download': False,
                'profile.default_content_setting_values.notifications': 2,
                'profile.default_content_setting_values.automatic_downloads': 1,

            })
            driver = webdriver.Chrome(service=ChromeService(
                ChromeDriverManager().install()), options=chrome_options)

            return driver

    def digitar_naturalmente(text, elemento):
        for letra in text:
            elemento.send_keys(letra)
            sleep(random.randint(1, 5)/30)

    text = "fizzvolibearshen@gmail.com"
    driver = iniciar_driver()
    driver.get('https://www.facebook.com/')
    sleep(3)
    driver.maximize_window()
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
    keywords = ["Lying client"]
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
    # Continue fazendo scroll e procurando divs até atingir o limite ou encontrar todas as divs desejadas
    while iteracao < max_iteracoes:
        divs = driver.find_elements(By.XPATH, "//div[@class='x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z']")
        cont = 0
        for div in divs:
            try:
                driver.implicitly_wait(20)
                comentario_element = div.find_element(By.XPATH, ".//span[contains(text(), 'comentário')]")
                comentario_texto = comentario_element.text
                print(f"Texto do Comentário: {comentario_texto}")
                comentario_element.click()
                sleep(20)
                posicao_inicial = 3

                # Encontre todos os elementos desejados
                elementos = driver.find_elements(By.XPATH, "//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u']")
                sleep(1)

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

                # Inicialize uma lista vazia para armazenar os textos
                textos = []
                contador = 0
                # Itere sobre os elementos a partir da posição inicial
                for elemento in elementos[posicao_inicial:]:
                    textos.append(elemento.text)
                    nova_variavel = textos.copy()
                    if any(keyword.lower() in nova_variavel.lower() for keyword in keywords):
                        resposta_aleatoria = random.choice(responses)
                        respond_list = driver.find_elements(By.XPATH, "//div[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xi81zsa x1xlr1w8']")
                        sleep(1)
                        respond = respond_list[contador]
                        respond.click()
                        sleep(7)
                        list_type_response = driver.find_elements(By.XPATH, "//div[@class='xzsf02u x1a2a7pz x1n2onr6 x14wi4xw notranslate']")
                        type_response = list_type_response.click[1]
                        sleep(1)
                        type_response.clear()
                        sleep(2)
                        digitar_naturalmente(resposta_aleatoria,type_response)
                        sleep(2)
                        list_send = driver.find_elements(By.XPATH, "//div[@class='x1ey2m1c xds687c xg01cxk x47corl x10l6tqk x17qophe x13vifvy x1ebt8du x19991ni x1dhq9h x1wpzbip x14yjl9h xudhj91 x18nykt9 xww2gxu']")
                        send = list_send[4]
                        sleep(1)
                        send.click()
                    del nova_variavel[0]
                    contador+=1

                # Agora, 'textos' contém os textos dos elementos a partir da posição [3]
                print(textos)
                sleep(2)
                
                exits = driver.find_element(By.XPATH, "//div[@class='x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 x14yjl9h xudhj91 x18nykt9 xww2gxu x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x78zum5 xl56j7k xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 xc9qbxq x14qfxbe x1qhmfi1']")

                exits.click()
                sleep(6)
                action = ActionChains(driver)
                for _ in range(16):
                    action.send_keys(Keys.DOWN).perform()
                sleep(2)
                cont+=1

            except:
                print("Campo de comentário não encontrado nesta div.")
                action = ActionChains(driver)
                for _ in range(16):
                    action.send_keys(Keys.DOWN).perform()
                sleep(2)
            cont += 1

        # Role para baixo para carregar mais divs
        sleep(3)  # Aguarde o carregamento das novas divs

        iteracao += 1
    print(cont)