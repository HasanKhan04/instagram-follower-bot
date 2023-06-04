from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_driver = webdriver.Chrome(options=chrome_options)

CHROME_DRIVER_PATH = r"C:\Users\hasan\Development\chromedriver.exe"
USERNAME = "hkpythonbot"
PASSWORD = "gwknass1"
SIMILAR_ACC = "coding.ninjas"


class InstaFollower:
    def __init__(self):
        service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=service)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
        login_btn.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACC}/followers/")
        time.sleep(2)


    def follow(self):
        time.sleep(2)
        followers = self.driver.find_elements(By.CSS_SELECTOR, 'li button')
        print(len(followers))
        for user in followers:
            user.click()
            time.sleep(2)




bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()

