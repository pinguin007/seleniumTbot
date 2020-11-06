from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import time
from followppl import follow_ppl
from search import Search
from profileList import myFollowingList

user=input("please enter your username:")
passkey=input("please enter your password:")

bot= webdriver.Firefox()
bot.get("https://www.twitter.com")
login= bot.find_element_by_xpath('//a[@href="/login"]')
login.click()
username= bot.find_element_by_name("session[username_or_email]")
username.send_keys(user)

password= bot.find_element_by_name("session[password]")
password.send_keys(passkey)
password.send_keys(Keys.ENTER)

time.sleep(7)

myFollowingList(bot,Keys,time)

time.sleep(6)

follow_ppl(bot,Keys,ActionChains,time)

time.sleep(6)

bot.close()

#it follows my best friends followers. I will add a feature to have it 

# follow back new followers
# unfollow anyone that didn't follow back in 3 days time
# like friends tweets