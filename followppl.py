from boundaryTest import is_in_boundary
from commaRemover import comma_remover

def follow_ppl(bot,Keys,ActionChains,time):
    firstfollowing= bot.find_elements_by_class_name("css-1dbjc4n.r-my5ep6.r-qklmqi.r-1adg3ll") #load a list of all the ppl I follow
    firstfollowing[0].click()       #select the first person on that list and click
    time.sleep(3)   

    num_followers= bot.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[5]/div[2]/a/span[1]/span").get_attribute('innerHTML')
    int_num_followers= comma_remover(num_followers)
    print(int_num_followers)

    followers= bot.find_element_by_partial_link_text("Followers") # we click the first person's followers page
    followers.send_keys(Keys.ENTER)
    time.sleep(6)
    
    counter=0
    scroll=0
    while(counter < int_num_followers):
   
        friends= bot.find_element_by_css_selector("div.r-1tlfku8:nth-child(1)").find_elements_by_xpath("//span[text()='Follow']")
        
        for i in friends:
            while not (is_in_boundary(bot,i)):
                scroll=bot.execute_script("return document.body.scrollHeight")
                bot.execute_script("window.scrollTo({}, document.body.scrollHeight)".format(scroll))
                time.sleep(1)
            
            ActionChains(bot).move_to_element(i).click().perform()
            counter+=1
            print(counter)
            time.sleep(1)

        bot.execute_script("window.scrollTo({}, document.body.scrollHeight)".format(scroll))
        
        time.sleep(3)
      