from instapy import InstaPy
#login
session = InstaPy(username = '#InstagramUserName', password = '#InstagramPaswword', headless_browser = False)
session.login()


session.unfollow_users(amount = 366,
                       allFollowing = True,
                       unfollow_after = 0,
                       sleep_delay = 600)
session.end()
