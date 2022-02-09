from bot.bot import Bot
import time

with Bot() as insta_bot:
    insta_bot.open_insta()
    insta_bot.login("username", "password")

    while True:
        # you can put as much as accounts u like in here to track
        insta_bot.first_search('account1', 'account2')
        insta_bot.second_search()
        insta_bot.excel()
