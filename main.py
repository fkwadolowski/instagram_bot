from selenium import webdriver
from selenium.webdriver.common.by import By
import time

SIMILAR_ACCOUNT = "xayoo777"
USERNAME = "antycwel12@gmail.com"
PASSWORD = "gitarasiemadab"
URL = "https://www.instagram.com/"


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(URL)
        accept_cookies = self.driver.find_element(
            By.XPATH,
            "/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]",
        )
        accept_cookies.click()
        time.sleep(1)
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys(USERNAME)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(PASSWORD)

        login_button = self.driver.find_element(
            By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div'
        )
        login_button.click()
        time.sleep(6)
        save_info = self.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button",
        )
        save_info.click()
        time.sleep(3)
        notif_button = self.driver.find_element(
            By.XPATH,
            "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]",
        )
        notif_button.click()

    def find_followers(self):
        self.driver.get(f"{URL}/{SIMILAR_ACCOUNT}")
        followers = self.driver.find_element(
            By.XPATH,
            '//*[@id="mount_0_0_j+"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[2]/div',
        )

    def follow(self):
        pass


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
