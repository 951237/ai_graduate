import time
import board
import adafruit_dht
import telebot

# 텔레그램 기본 설정
API_KEY = '1644820427:AAEllDn4xGfRAFHGpb9lFxx5QsK-__AG7L8'  # 텔레그램봇 코딩951237 bot api
bot = telebot.TeleBot(API_KEY)
chat_id = '428116987'
dhtDevice = adafruit_dht.DHT22(board.D4)

# menu 명령어로 전체 명령어 보여주기


# hello World!
@bot.message_handler(commands=['pi'])
def greet(message):
      bot.reply_to(message, "Hello! Pi world!")

@bot.message_handler(commands=['tmp'])
def check_temp(message):
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        result = "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity )
        bot.send_message(message.chat.id, result)

    except RuntimeError as error:
        bot.send_message(message.chat.id, error.args[0])
        detDevice.exit()
    
bot.polling()

                                                                                                               
