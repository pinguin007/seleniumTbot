def myFollowingList(bot,Keys,time):
    profile= bot.find_element_by_link_text("Profile")
    print("{}".format(profile))
    profile.send_keys(Keys.ENTER)
    time.sleep(3)

    following= bot.find_element_by_partial_link_text("Following")
    following.send_keys(Keys.ENTER)
    time.sleep(3)