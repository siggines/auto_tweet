from selenium import webdriver
from time import sleep

# This script will log in to twiiter and tweet something of your choice.

# Put in your username, password, and your tweet in place of the comments.

class TwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://twitter.com')
        sleep(2)
        login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div/div[1]/div/div/div[1]/a/div')
        login.click()
        email_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
        email_input.send_keys(#'Email goes here')
        pw_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')
        pw_input.send_keys(#'Password goes here')
        login_submit = bot.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div')
        login_submit.click()

    def tweet(self):
        sleep(2)
        click_tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div/div[3]/a/div')
        click_tweet.click()
        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
        tweet.send_keys(#'Tweet goes here')
        tweet_submit = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]')
        tweet_submit.click()

bot = TwitterBot()
bot.login()
bot.tweet()
