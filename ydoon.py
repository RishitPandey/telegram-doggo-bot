from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

allowed_extensions = ['jpg', 'png', 'jpeg']

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url



def bop(bot, update):
    url = get_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('1110418301:AAEy76PA31Go_IapaTyXRAILo-1yyA301Mw')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()