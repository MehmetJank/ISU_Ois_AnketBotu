from selenium import webdriver # for webdriver
from selenium.webdriver.common.by import By # for specifying locators
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


user_name = "okulnumara" # for entering the username okul nonuzu girin
user_password = "password" # for entering the password sisteme giriş yaparken kullandığınız şifrenizi girin


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://ois.istinye.edu.tr/auth/login") # for opening the website 

time.sleep(1)

user_login = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[1]/form/div[2]/div[3]/input[2]'))

user_login.send_keys(user_name)
print("user_login")

password_login = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[1]/form/div[2]/div[3]/input[3]'))

password_login.send_keys(user_password)
print("password_login")

login_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[1]/form/div[2]/div[3]/button')).click()
print("login_click")

time.sleep(1)

dogrulama_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[3]/input')).click()
print("dogrulama_click")


for i in range(1, 6):
    time.sleep(3)
    print("Basliyor Ders " + str(i))
    a1_click =  WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[1]/ol/li[1]/select')).click()
    print("a1_click")
    a1_secim_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[1]/ol/li[1]/select/option[4]')).click()
    print("a1_secim_click")
    a2_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[1]/ol/li[2]/select')).click()
    print("a2_click")
    a2_secim_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[1]/ol/li[2]/select/option[4]')).click()
    print("a2_secim_click")
    a3_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[1]/ol/li[3]/select')).click()
    print("a3_click")
    a3_secim_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[1]/ol/li[3]/select/option[4]')).click()
    print("a3_secim_click")                                                                 
    a4_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[1]/ol/li[4]/select')).click()
    print("a4_click")
    a4_secim_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[1]/ol/li[4]/select/option[4]')).click()
    print("a4_secim_click")

    b1_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[2]/ol/li[1]/select')).click()
    print("b1_click")
    b1_secim_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[2]/ol/li[1]/select/option[4]')).click()
    print("b1_secim_click")                                                         
    b2_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[2]/ol/li[2]/select')).click()
    print("b2_click")                                                                       
    b2_secim_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[2]/ol/li[2]/select/option[4]')).click()
    print("b2_secim_click")
    b3_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[2]/ol/li[3]/select')).click()    
    print("b3_click")
    b3_secim_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[2]/ol/li[3]/select/option[4]')).click()
    print("b3_secim_click")
    b4_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[2]/ol/li[4]/select')).click()
    print("b4_click")
    b4_secim_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[2]/ol/li[4]/select/option[4]')).click()
    print("b4_secim_click")
    b5_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[2]/ol/li[5]/select')).click()
    print("b5_click")
    b5_secim_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[2]/ol/li[5]/select/option[4]')).click()
    print("b5_secim_click")

    c1_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[3]/ol/li[1]/select')).click()
    print("c1_click")
    c1_secim_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[3]/ol/li[1]/select/option[4]')).click()
    print("c1_secim_click")
    c2_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[3]/ol/li[2]/select')).click()
    print("c2_click")
    c2_secim_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[3]/ol/li[2]/select/option[4]')).click()
    print("c2_secim_click")
    c3_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[3]/ol/li[3]/select')).click()
    print("c3_click")
    c3_secim_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/fieldset[3]/ol/li[3]/select/option[4]')).click()
    print("c3_secim_click")

    gonder_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/form/p/input')).click()
    print("gonder_click")

    time.sleep(1)

    try:
        onaylama_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[5]/div[3]/a')).click()
        print("onaylama_click")
    except:
        onaylama3_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[6]/div[3]/a')).click()
        print("onaylama_click hata")

    time.sleep(1)
    
    try:
        onaylama2_click = WebDriverWait(driver, 45).until(lambda x: x.find_element(By.XPATH, '/html/body/div[5]/div[3]/button')).click()
        print("onaylama2_click")
    except:
        print("onaylama2_click hata")
    
driver.close()