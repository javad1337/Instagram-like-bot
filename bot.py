from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def login(browser):

    browser.get("https://www.instagram.com/?hl=en")
    time.sleep(1)
    username = browser.find_element_by_css_selector("[name='username']")
    password = browser.find_element_by_css_selector("[name='password']")
    login = browser.find_element_by_css_selector("button")
    username.send_keys("1")  # Replace 1 with your instagram username
    password.send_keys("2")  # Replace 2 with your instagram password
    login.click()


    time.sleep(1)

def Visit_tag(browser, url):
    browser.get(url)
    time.sleep(1)

    pictures = browser.find_elements_by_css_selector("div[class='_9AhH0']")

    count=0

    for pic in pictures:
        if count>=3:
            break

        pic.click()

        time.sleep(1)

        heart = browser.find_element_by_css_selector("[aria-label='Like']")
        heart.click()

        close = browser.find_element_by_css_selector("[aria-label='Close']")
        close.click()

        count+=1



def main():
    browser= webdriver.Chrome()
    login(browser)

    tags = [
        "programming",
        "programminglife",
        "programmerslife",
        "softwaredeveloper",
        "programmerlife",
        "developerlife",
        "programmers",
    ]

# You can write any hashtag you want in tags

    for tag in tags:
         Visit_tag(browser, f"https://www.instagram.com/explore/tags/{tag}")


main()