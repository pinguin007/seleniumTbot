def Search(bot, text, time):
    #bot= webdriver.Firefox()
    bot.get("https://twitter.com/search?q="+text+"&src=typd")
    time.sleep(6)