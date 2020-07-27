from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

bot= webdriver.Firefox()
bot.get("https://www.twitter.com")
username= bot.find_element_by_name("session[username_or_email]")
username.send_keys("haneke1091@lercjy.com")

password= bot.find_element_by_name("session[password]")
password.send_keys("777123999Aaa!")
password.send_keys(Keys.ENTER)

time.sleep(7)

def Search(text):
    bot.get("https://twitter.com/search?q="+text+"&src=typd")
    time.sleep(6)


#Search("kobe")

def followpage():
    profile= bot.find_element_by_link_text("Profile")
    print("{}".format(profile))
    profile.send_keys(Keys.ENTER)
    time.sleep(3)

    following= bot.find_element_by_partial_link_text("Following")
    following.send_keys(Keys.ENTER)
    time.sleep(3)


def followppl():
    firstfollowing= bot.find_elements_by_class_name("css-1dbjc4n.r-my5ep6.r-qklmqi.r-1adg3ll") #load a list of all the ppl I follow
    firstfollowing[0].click()       #select the first person on that list and click
    time.sleep(3)   

    num_followers= bot.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[5]/div[2]/a/span[1]/span").get_attribute('innerHTML')
    int_num_followers= commaRemover(num_followers)
    print(int_num_followers)

    followers= bot.find_element_by_partial_link_text("Followers") # we click the first person's followers page
    followers.send_keys(Keys.ENTER)
    time.sleep(6)
    
    counter=0
    scroll=0
    while(counter <= int_num_followers):
       
        friends= bot.find_element_by_css_selector("div.r-1tlfku8:nth-child(1)").find_elements_by_xpath("//span[text()='Follow']")
        
        for i in friends:
            print(i.get_attribute('innerHTML'))
            counter+=1
            print(counter)
        bot.execute_script("window.scrollTo({}, document.body.scrollHeight)").format(scroll)
        scroll=bot.execute_script("return document.body.scrollHeight")
        #time.sleep(2)

    '''while(counter < int_num_followers):
        firstUserfollowers= bot.find_element_by_css_selector("div.r-1tlfku8:nth-child(1)")
        fuf2= firstUserfollowers.find_elements_by_class_name("css-1dbjc4n.r-my5ep6.r-qklmqi.r-1adg3ll")
        print(fuf2)
        for i in range(len(fuf2)):
            innerText=fuf2[i].find_element_by_xpath("//span[text()='Follow']")
            #innerText[1].click()
            print(innerText.get_attribute('innerHTML'))
            counter+=1
            print(counter)
            #time.sleep(2.5)
        
        bot.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3)'''

def commaRemover(text):
    list_version= list(text)
    for i in  list_version:
        if i==',':
            list_version.remove(i)
    finalnum= ''.join(list_version)

    return int(finalnum)


followpage()

time.sleep(6)

followppl()
time.sleep(6)
bot.close()
# once I go to my following page: 
# I will get a list of all the people I follow 
# I will go to the first person's profile
#I will click on the followers link text
#let the page load
#get a list of all the people in the follwers page, and use counter
# loop through all of them
# follow everyone on the page 
#after following, make a list[while person not in "following list"]
# scroll the page to load more people
# repeat until we have followed everyone, there isn't "follow", and we can't scroll down anymore. or the number of people bot follows is equal to the number blik follows
#bot.close()

#examples for the following blik's followers loop, while(count <= followercount 365){get follower list, follow all of them(sleep between each 2s), scroll-down(sleep again), count++}

##NOTE: use find element css class joining rule to find specific class within a class by joining spaces with "."

#find_element_by_css_selector("css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")
#find_element_in_class("css-1dbjc4n")