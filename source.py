# import telepot
# bot = telepot.Bot('387068894:AAHxbcwFL8zUiwb3JLc7TnUeKP5Pu8GPZig')
# print(bot.getUpdates(9572204+1))

import sys
import time
import telepot
from telepot.loop import MessageLoop

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text'])

TOKEN = '387068894:AAHxbcwFL8zUiwb3JLc7TnUeKP5Pu8GPZig'  # get token from command-line

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)