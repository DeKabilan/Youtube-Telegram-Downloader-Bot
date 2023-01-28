import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from yt import download
import time
import os
from dotenv import load_dotenv

load_dotenv()

tokens= os.getenv("bottoken")


bot = telebot.TeleBot(tokens)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id,"Support the Dev: www.github.com/DeKabilan")




@bot.message_handler(func=lambda msg: msg)
def sendres(message):
    link=message.text
    if "youtu" in message.text:
        bot.delete_message(message.chat.id,message.message_id)
        bot.send_message(message.chat.id,link,reply_markup= markup_inline())
    else:
        bot.reply_to(message,"Link is Invalid")


@bot.callback_query_handler(func=lambda message : True)
def callback_query(call):
    link = call.message.text
    if call.data == "720p":
        bot.delete_message(call.message.chat.id,call.message.message_id)
        dlres="720p"
        dl=bot.send_message(call.message.chat.id,"Downloading . . .")
        bot.send_message(call.message.chat.id,download(link,dlres))
        bot.delete_message(call.message.chat.id,dl.id)
    if call.data == "1080p":
        bot.delete_message(call.message.chat.id,call.message.message_id)
        dlres="1080p"
        dl=bot.send_message(call.message.chat.id,"Downloading . . .")
        bot.send_message(call.message.chat.id,download(link,dlres))
        bot.delete_message(call.message.chat.id,dl.id)
    if call.data == "240p":
        bot.delete_message(call.message.chat.id,call.message.message_id)
        dlres="240p"
        dl=bot.send_message(call.message.chat.id,"Downloading . . .")
        bot.send_message(call.message.chat.id,download(link,dlres))
        bot.delete_message(call.message.chat.id,dl.id)
    if call.data == "360p":
        bot.delete_message(call.message.chat.id,call.message.message_id)
        dlres="360p"
        dl=bot.send_message(call.message.chat.id,"Downloading . . .")
        bot.send_message(call.message.chat.id,download(link,dlres))
        bot.delete_message(call.message.chat.id,dl.id)
    if call.data == "480p":
        bot.delete_message(call.message.chat.id,call.message.message_id)
        dlres="480p"
        dl=bot.send_message(call.message.chat.id,"Downloading . . .")
        bot.send_message(call.message.chat.id,download(link,dlres))
        bot.delete_message(call.message.chat.id,dl.id)
    return dlres

def markup_inline():
    markup = InlineKeyboardMarkup()
    markup.width = 2
    markup.add(InlineKeyboardButton("1080p", callback_data="1080p"))
    markup.add(InlineKeyboardButton("720p", callback_data="720p"))
    markup.add(InlineKeyboardButton("480p", callback_data="480p"))
    markup.add(InlineKeyboardButton("360p", callback_data="360p"))

    return markup
     

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(5)
  