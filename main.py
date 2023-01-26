import telebot
import os
from yt import download
import time

tokens="5947596707:AAERSl_x9nNHpdqc4b_h9DdO8cUq1DY52Y4"

bot = telebot.TeleBot(tokens)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id,"Support the Dev: www.github.com/DeKabilan")
    

@bot.message_handler(func=lambda msg: msg)
def sendlink(message):
    if ".youtu" in message.text:
        bot.reply_to(message,download(message.text,"720p"))
    else:
        bot.reply_to(message,"Link is Invalid")


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(5)
  