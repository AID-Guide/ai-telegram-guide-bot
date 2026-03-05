import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я AI гид по Паттайе 🇹🇭")

@bot.message_handler(func=lambda message: True)
def reply(message):
    bot.send_message(message.chat.id, "Скоро я стану умным AI гидом 😎")

bot.polling()
