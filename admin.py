import telebot

from config import BOT_TOKEN
from config import ADMIN_ID
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(content_types=["text"])
def message(text):
    bot.send_message(ADMIN_ID, text)


@bot.message_handler(content_types=["photo"])
def photo1(chat_id):
    photo = open('images/image1.jpg', 'rb')
    bot.send_photo(chat_id=chat_id, photo=photo)


@bot.message_handler(content_types=["photo"])
def photo2(chat_id):
    photo = open('images/image2.jpg', 'rb')
    bot.send_photo(chat_id=chat_id, photo=photo)


@bot.message_handler(content_types=["photo"])
def photo3(chat_id):
    photo = open('images/image3.jpg', 'rb')
    bot.send_photo(chat_id=chat_id, photo=photo)


@bot.message_handler(content_types=["photo"])
def photo4(chat_id):
    photo = open('images/image4.jpg', 'rb')
    bot.send_photo(chat_id=chat_id, photo=photo)


@bot.message_handler(content_types=["photo"])
def photo5(chat_id):
    photo = open('images/image5.jpg', 'rb')
    bot.send_photo(chat_id=chat_id, photo=photo)


@bot.message_handler(content_types=["file"])
def sogl(chat_id):
    photo = open('images/soglasie_na_pd.docx', 'rb')
    bot.send_document(chat_id=chat_id, document=photo)


@bot.message_handler(content_types=["photo"])
def photo6(chat_id):
    photo = open('images/image6.jpg', 'rb')
    bot.send_photo(chat_id=chat_id, photo=photo)


@bot.message_handler(content_types=["photo"])
def photo7(chat_id):
    photo = open('images/image7.jpg', 'rb')
    bot.send_photo(chat_id=chat_id, photo=photo)
