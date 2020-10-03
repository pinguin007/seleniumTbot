def is_in_boundary(bot, profile):
    profile_left_bound = profile.location.get('x')
    profile_top_bound = profile.location.get('y')
    profile_width = profile.size.get('width')
    profile_height = profile.size.get('height')
    profile_right_bound = profile_left_bound + profile_width
    profile_lower_bound = profile_top_bound + profile_height

    win_upper_bound = bot.execute_script('return window.pageYOffset')
    win_left_bound = bot.execute_script('return window.pageXOffset')
    win_width = bot.execute_script('return document.documentElement.clientWidth')
    win_height = bot.execute_script('return document.documentElement.clientHeight')
    win_right_bound = win_left_bound + win_width
    win_lower_bound = win_upper_bound + win_height

    return all((win_left_bound <= profile_left_bound,
                win_right_bound >= profile_right_bound,
                win_upper_bound <= profile_top_bound,
                win_lower_bound >= profile_lower_bound)
              )