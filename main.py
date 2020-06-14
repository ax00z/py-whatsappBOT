'''
Whatsapp auto-reply bot

'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = ("D:\Downloads\Compressed\chromedriver\chromedriver.exe") # Set this path to your browser driver executable
SITE = "https://web.whatsapp.com/"

browser = webdriver.Chrome(PATH)
browser.get(SITE)

time.sleep(5)

target = input("Enter your target contact")

names = list()

for target in names:

    name = target
    person = browser.find_element_by_xpath('//span[@title = "{}"]'.format(target))
    person.click()  

    for i in range(1,3):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    msg_got = browser.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
    msg = [message.text for message in msg_got]

    try:

        if name: # Comment out if you wish to reply to a specific message
        
        # if msg[-1] == "Target message here": (Uncomment to change the detected message that you wish to reply to)
    
            reply = "" # Your reply

            inp = browser.find_element_by_class_name('_3uMse')
            inp.click()
            inp.send_keys(reply)
            inp.send_keys(Keys.ENTER)

        # auto-reply for any message

        else :

            other_reply = ""
            
            inp = browser.find_element_by_class_name('_3uMse')
            inp.click()
            inp.send_keys(other_reply)
            inp.send_keys(Keys.ENTER)