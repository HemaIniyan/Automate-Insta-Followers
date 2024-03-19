from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)
USERNAME = "hemalathainiyan"
PASSWORD = "Inika@$2651"
SIMILAR_ACCOUNT = "chefsteps"


class InstaFollower:
    def __init__(self):
        self.driver = driver

    def login(self):
        sleep(5)
        username_text = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_text.send_keys(USERNAME)
        password_text = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_text.send_keys(PASSWORD)
        password_text.send_keys(Keys.ENTER)
        sleep(5)
        not_now_btn = self.driver.find_element(By.CSS_SELECTOR, value="._ac8f div")
        not_now_btn.click()

    def find_followers(self):
        self.driver.get(" https://www.instagram.com/chefsteps/")
        sleep(3)
        decline_btn = self.driver.find_elements(By.CSS_SELECTOR, value="div button")
        decline_btn[-1].click()
        sleep(5)
        login_btn = self.driver.find_elements(By.CSS_SELECTOR, value="div a")
        login_btn[-2].click()
        self.login()
        sleep(5)
        followers_link = self.driver.find_element(By.CSS_SELECTOR, value="li a")
        followers_link.click()
        sleep(5)
        pop_up = self.driver.find_element(By.XPATH, value='/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop_up)
            sleep(2)

    def follow(self):
        sleep(5)
        print("Follow all account")
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value="._acan")
        for button in all_buttons:
            try:
                # button.click()
                print(button.text)
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, value='/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()
                sleep(2)


bot = InstaFollower()
bot.find_followers()
bot.follow()
