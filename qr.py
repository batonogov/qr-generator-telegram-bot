# Телеграм бот отвечающий qr кодами на сообщения

import telebot, qrcode, os # Импортируем необходимые библиотеки


token = os.getenv('qr_token')
bot = telebot.TeleBot(token) # Указываем token

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я готов.')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    user_input = '{0}'.format(message.text) # Получаем введенный текст
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_M,
        box_size = 6,
        border = 0, # Рамка qr кода
    )
    qr.add_data(user_input) 
    qr.make(fit = True)
    img = qr.make_image()
    img.save('qr.png')
    qr = open('qr.png', 'rb')
    bot.send_document(message.chat.id, qr)

bot.polling()
