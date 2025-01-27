# pip install transformers
# pip install torch
# pip install selenium

from transformers import pipeline
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from collections import Counter

def coletar_reviews(url, num_reviews=10):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver,10)
    reviews = []
    
    print(f"Coletando reviews de: {url}")
    
    try:
        driver.get(url)
        review_items = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".ui-review-capability-comments p")
            )
        )
        
        while len(reviews) < num_reviews:
            for item in review_items:
                review = item.text.strip()
                if review and review not in reviews:
                    reviews.append(review)
                    print(f"Coletado review ({len(reviews)} / {num_reviews})")
                    if len(reviews) >= num_reviews:
                        break
            if len(reviews) < num_reviews:
                driver.execute_script(
                    "window.scrollTo(0,document.body.scrollHeight);"
                )
                time.sleep(2)
                review = driver.find_elements(
                    By.CSS_SELECTOR, ".ui-review-capability-comments p"
                )
    except TimeoutException:
        print("Timeout ao carregar reviews")
    except Exception as e:
        print("Erro no scraping: {e}")
    finally:
        driver.quit()
        
    return reviews

url = input("Digite a URL do produto:")
num_reviews = int(input("Quantas reviews deseja analisar?"))

print(coletar_reviews(url, num_reviews))
                