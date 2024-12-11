import os
import telebot
from config import TOKEN, API_URL, API_KEY, SECRET_KEY
from telebot.types import Message
from main import generate_image_from_text
import base64
from PIL import Image
from io import BytesIO


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['image'])
def gen_image(msg: Message):
    bot.send_message(msg.chat.id, "Напиши что ты хочешь сгенерировать?❤")
    bot.register_next_step_handler(msg, gen_promt)


def gen_promt(msg:Message):
    promt = msg.text
    bot.send_message(msg.chat.id, "Началась генерация картинки🌆")
    image = generate_image_from_text(promt, API_URL, API_KEY, SECRET_KEY)[0]
    data = base64.b64decode(image)
    image = Image.open(BytesIO(data)) 
    image.save("photo.jpg")
    with open('photo.jpg', 'rb') as file:
        photo = file.read()
        bot.send_photo(msg.chat.id,photo=photo)





bot.infinity_polling()