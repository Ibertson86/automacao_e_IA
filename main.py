from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def pesquisa_google():
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://br.search.yahoo.com")
        campo_pesquisa = driver.find_element(By.CLASS_NAME, "sbq")
        campo_pesquisa.send_keys("Infinity School")
        campo_pesquisa.send_keys(Keys.ENTER)
        sleep(5)
        titulo = driver.title
        print(f"Título da página: {titulo}")
    finally:
        driver.quit()
        
def login():
    driver = webdriver.Chrome()
    try:
        driver.get("https://the-internet.herokuapp.com/login")
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        username.send_keys("tomsmith")
        password.send_keys("SuperSecretPassword!")
        sleep(3)
        driver.find_element(By.CSS_SELECTOR, "button.radius").click()
        sleep(3)
    finally:
        driver.quit()
        
def preencher_form():
    driver = webdriver.Chrome()
    try:
        driver.get("https://the-internet.herokuapp.com/login")
        campos = {
            "nome": "João",
            "email": "joao@joao.com",
            "telefone": "8199995959"
        }
        
        for campo, valor in campos.items():
            try:
                elemento = driver.find_element(By.NAME, campo)
                elemento.clear()
                elemento.send_keys(valor)
                print(f"Campo {campo} preenchido com sucesso")
            except:
                print(f"Campo {campo} não foi encontrado")
                sleep(3)
    finally:
        driver.quit()

# pesquisa_google()
# login()
preencher_form()
    