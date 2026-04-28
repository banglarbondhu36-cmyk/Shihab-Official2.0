import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from flask import Flask
import threading
import os

# আপনার বটের টোকেন
TOKEN = '8688194468:AAHRvVpTcB7yYrFGi5idbF6flhZFkB5eZ_Y'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# রেন্ডার সার্ভার চালু রাখার জন্য
@app.route('/')
def index():
    return "Bot is alive and running!"

# ১. বট স্টার্ট করলে যা হবে
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # কীবোর্ডে 'ওয়ালাইকুম আসসালাম' বাটন তৈরি
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = KeyboardButton("ওয়ালাইকুম আসসালাম")
    markup.add(btn1)
    
    # বটের সালাম
    bot.send_message(message.chat.id, "আসসালামুয়ালাইকুম", reply_markup=markup)

# ২. বাটনে ক্লিক করার পর বটের উত্তর
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    
    if message.text == "ওয়ালাইকুম আসসালাম":
        # উইকলি নেওয়ার বাটন তৈরি
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn2 = KeyboardButton("আমি ফ্রি ফায়ারে উইকলি নিতে চাই")
        markup.add(btn2)
        
        bot.send_message(message.chat.id, "কীভাবে সাহায্য করতে পারি?", reply_markup=markup)
        
    elif message.text == "আমি ফ্রি ফায়ারে উইকলি নিতে চাই" or message.text == "আমি উইকলি নিতে চাই":
        # ফাইনাল মেসেজ (বাটন সরিয়ে দেওয়া হবে)
        from telebot.types import ReplyKeyboardRemove
        remove_markup = ReplyKeyboardRemove()
        
        bot.send_message(message.chat.id, "আপনার উইকলি পেন্ডিংয়ে আছে দয়া করে অপেক্ষা করুন", reply_markup=remove_markup)

# বট এবং সার্ভার একসাথে চালানোর কমান্ড
def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
